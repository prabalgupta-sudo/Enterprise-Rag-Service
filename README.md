# 🚀 Enterprise GenAI RAG Platform on Kubernetes

Production-grade Retrieval-Augmented Generation (RAG) system deployed on Kubernetes.

This project demonstrates how to build, containerize, and deploy a scalable GenAI microservice using modern cloud-native tooling.

---

## 🧱 Architecture

- FastAPI microservice for API layer
- SentenceTransformers for embeddings
- Qdrant vector database for semantic search
- OpenAI LLM for response generation
- Docker for containerization
- Kubernetes (MicroK8s) for orchestration
- Secrets management via Kubernetes Secrets

---

## ⚙️ Tech Stack

| Layer | Technology |
|--------|------------|
| API | FastAPI |
| Embeddings | SentenceTransformers |
| Vector DB | Qdrant |
| LLM | OpenAI |
| Container | Docker |
| Orchestration | Kubernetes |
| OS | Ubuntu |

---

## ✨ Features

- 📄 Upload documents
- 🔎 Semantic search using vector embeddings
- 🤖 Context-aware question answering (RAG)
- 🔐 Secure API key handling
- ☸️ Kubernetes-native deployment
- 🚀 Scalable microservice architecture

---

## 🛠️ Local Development

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
