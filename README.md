# 📚 RAG Chatbot 🔍 🤖 — Powered by LLaMA 3 on Groq

Welcome to **Deepan's RAG Chatbot**, a lightweight, efficient Retrieval-Augmented Generation (RAG) chatbot that supports **PDF**, **text**, and **image (OCR)** uploads. This app uses the power of **LLaMA 3 hosted via Groq API**, **FAISS** for vector search, and **Sentence Transformers** for document embeddings.

---

## 🚀 Features

- 🔍 Upload and process multiple file types: `.txt`, `.pdf`, `.jpg`, `.jpeg`
- 📑 Extract text from documents and images (OCR with Tesseract)
- 🧠 Embed documents using `all-MiniLM-L6-v2`
- 📚 Vector store using FAISS for semantic similarity search
- 💬 Interactive Streamlit chat interface
- 🤖 LLM responses generated via **Groq-hosted LLaMA 3 (8B)**

---

## 🧰 Tech Stack

| Component       | Library/Tool                             |
|-----------------|-------------------------------------------|
| UI              | Streamlit                                |
| Embeddings      | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector Search   | FAISS                                     |
| OCR             | PyTesseract                               |
| PDF Reading     | PyPDF2                                    |
| LLM             | Groq API (LLaMA 3)                        |
| Image Handling  | Pillow (`PIL`)                            |
| API Secrets     | dotenv (`.env` file for config)           |

---

## 📝 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rag-chatbot-groq.git
cd rag-chatbot-groq
