# 🚀 Enterprise RAG Service (GenAI + Kubernetes)

A production‑ready **Retrieval Augmented Generation (RAG)** platform built with **FastAPI, Qdrant Vector DB, Sentence Transformers, Docker, and Kubernetes (MicroK8s)**.
This project demonstrates how to design and deploy an enterprise‑grade GenAI system with scalable infrastructure and clean MLOps practices.

---

## 🌟 Key Features

* 🔎 **Semantic Search & RAG** using Qdrant vector database
* 🤖 **LLM Integration** (OpenAI compatible)
* ⚡ **FastAPI Microservice** for ingestion and querying
* 🧠 **Sentence Transformers Embeddings**
* 🐳 **Dockerized Services**
* ☸️ **Kubernetes Deployment (MicroK8s)**
* 📈 **Enterprise‑ready architecture**

---

## 🏗️ Architecture

```
User
  │
  ▼
FastAPI (RAG Service)
  │
  ├── Embedding Model (SentenceTransformers)
  │
  ├── Vector Search → Qdrant
  │
  └── LLM Completion → OpenAI
  │
  ▼
Answer Response
```

**Flow:**

1. User uploads documents.
2. Text is embedded and stored in Qdrant.
3. User asks a question.
4. Similar vectors retrieved from Qdrant.
5. Context passed to LLM.
6. Answer returned via API.

---

## 🧱 Tech Stack

| Layer            | Technology            |
| ---------------- | --------------------- |
| API              | FastAPI               |
| Embeddings       | SentenceTransformers  |
| Vector DB        | Qdrant                |
| LLM              | OpenAI API            |
| Containerization | Docker                |
| Orchestration    | Kubernetes (MicroK8s) |
| Language         | Python 3.12           |

---

## 📦 Repository Structure

```
rag-service/
│
├── main.py                # FastAPI application
├── requirements.txt       # Python dependencies
├── Dockerfile              # Container build
├── rag.yaml                # Kubernetes manifest
├── sample.txt              # Test data
├── README.md               # Documentation
└── .gitignore
```

---

## ⚙️ Local Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/Enterprise-Rag-Service.git
cd Enterprise-Rag-Service
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create `.env`:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 4️⃣ Run Qdrant (Docker)

```bash
docker run -d -p 6333:6333 qdrant/qdrant
```

Verify:

```
http://localhost:6333
```

---

### 5️⃣ Run API Server

```bash
uvicorn main:app --reload
```

Open API Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Usage

### 📤 Upload Document

```
POST /upload
FormData: file=<text file>
```

Response:

```json
{"status": "uploaded"}
```

---

### ❓ Ask Question

```
GET /ask?query=Your question
```

Response:

```json
{
  "answer": "Generated answer from knowledge base"
}
```

---

## ☸️ Kubernetes Deployment (MicroK8s)

### Build Image

```bash
docker build -t rag-service:1.0 .
```

Export image:

```bash
docker save rag-service:1.0 -o rag-service.tar
sudo microk8s ctr image import rag-service.tar
```

Apply deployment:

```bash
sudo microk8s kubectl apply -f rag.yaml
```

Verify:

```bash
sudo microk8s kubectl get pods -n genai
```

Port Forward:

```bash
sudo microk8s kubectl port-forward -n genai svc/qdrant 6333:6333
```

---

## 🔐 Security Notes

* Never commit `.env` files
* API keys are loaded via environment variables
* `.gitignore` prevents secrets and venv from being committed

---

## 🎯 Learning Outcomes

This project demonstrates:

* Enterprise GenAI architecture
* Vector search fundamentals
* RAG pipelines
* Docker + Kubernetes deployment
* Production API design
* Debugging real infrastructure issues

---

## 🛣️ Future Enhancements

* ✅ Authentication & RBAC
* ✅ Streaming responses
* ✅ Chunking large documents
* ✅ Observability (Prometheus + Grafana)
* ✅ CI/CD Pipeline
* ✅ Multi‑tenant collections

---

## 👨‍💻 Author

**Prabal Gupta**
AI Engineer | Cloud | Kubernetes | GenAI

---

⭐ If you find this project useful, give it a star on GitHub!
