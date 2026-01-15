from fastapi import FastAPI, UploadFile, File
from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv
import os
import uuid
import requests


# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="Enterprise RAG API")

# =========================
# Configuration
# =========================
QDRANT_URL = "http://localhost:6333"
COLLECTION = "documents"

client = QdrantClient(
    url=QDRANT_URL,
    check_compatibility=False
)

embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize OpenAI client with API key from environment
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Verify API key is loaded
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set!")




# =========================
# Startup
# =========================
@app.on_event("startup")
def setup_collection():
    collections = client.get_collections().collections
    existing = [c.name for c in collections]

    if COLLECTION not in existing:
        client.create_collection(
            collection_name=COLLECTION,
            vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE)
        )

# =========================
# Upload Endpoint
# =========================
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    text = (await file.read()).decode()
    vector = embedder.encode(text).tolist()

    client.upsert(
        collection_name=COLLECTION,
        points=[
            models.PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={"text": text}
            )
        ]
    )

    return {"status": "uploaded"}

# =========================
# Ask Endpoint
# =========================
@app.get("/ask")
def ask(query: str):
    q_vector = embedder.encode(query).tolist()

    # Use direct HTTP API for Qdrant search
    response = requests.post(
        f"{QDRANT_URL}/collections/{COLLECTION}/points/search",
        json={
            "vector": q_vector,
            "limit": 3,
            "with_payload": True
        }
    )
    
    result = response.json()
    
    if result.get("status") != "ok":
        return {"error": "Search failed", "details": result}
    
    hits = result.get("result", [])

    if not hits:
        return {"answer": "No relevant documents found in the knowledge base."}

    # Extract context from results
    context = "\n\n".join([hit["payload"]["text"] for hit in hits])

    prompt = f"""Answer strictly using the context below.

Context:
{context}

Question:
{query}
"""

    # Updated OpenAI API call (v1.0.0+)
    openai_response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "answer": openai_response.choices[0].message.content,
        "sources_count": len(hits)
    }


@app.get("/test-openai")
def test_openai():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {"error": "API key not found"}
    return {
        "api_key_loaded": True,
        "key_prefix": api_key[:10] + "..." if api_key else None
    }