# 📚 RAG Chatbot 🔍 🤖 — Powered by LLaMA 3 on Groq

Welcome to **Deepan's RAG Chatbot**, a lightweight, efficient Retrieval-Augmented Generation (RAG) chatbot that supports **PDF**, **text**, and **image (OCR)** uploads. This app uses the power of **LLaMA 3 hosted via Groq API**, **FAISS** for vector search, and **Sentence Transformers** for document embeddings.

![banner](https://img.shields.io/badge/Powered%20By-Groq%20%2B%20LLaMA3-brightgreen)  
🔗 Hosted on GitHub: [Deeps72-ux/RAG-model](https://github.com/Deeps72-ux/RAG-model)

---

## 🚀 Features

- 📁 Upload and process multiple file types: `.txt`, `.pdf`, `.jpg`, `.jpeg`
- 🔍 OCR support using Tesseract for image files
- 🧠 Embed documents using `all-MiniLM-L6-v2` from Sentence Transformers
- 📚 FAISS vector store for fast semantic search
- 💬 Interactive Streamlit chat interface
- 🤖 Contextual responses generated via **Groq-hosted LLaMA 3 (8B)**
- 💬 Memory of chat history

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

## 📁 File Structure
RAG-model/ <br>
├── app.py # Main Streamlit application  <br>
├── requirements.txt <br>
├── .env # Groq API key (excluded from Git) <br>
└── README.md <br>

---

## 📝 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Deeps72-ux/RAG-model.git
cd RAG-model
```

### 2. Create and Activate a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Requirements
``` bash
pip install -r requirements.txt
```
### 4. Install Tesseract OCR

Ubuntu/Debian:
``` bash
sudo apt install tesseract-ocr
macOS:

``` bash
brew install tesseract
```
Windows: Download and install from: https://github.com/tesseract-ocr/tesseract/wiki

### 🔐 Environment Variables
Create a .env file in the root of your project:

ini

GROQ_API_KEY=your_groq_api_key_here
⚠️ Important: Never expose your .env file in public repositories. Add .env to .gitignore.

### ▶️ Running the App
``` bash
streamlit run app.py
```
You’ll be greeted with:

```bash
🌟 Deepan's RAG Chatbot welcomes you 🙂
📎 Upload files and ask questions with real context!
```

### 💡 Sample Workflow
Upload one or more .txt, .pdf, or .jpg files.

Click "📚 Process Files" to embed them using Sentence Transformers.

Ask any question in the chat box.

Get a concise and relevant answer generated with RAG + Groq's LLaMA 3.

### 🧪 Example Use Cases
Chat with your academic PDFs or scanned notes.

Ask questions from invoices or image-based documents.

Build personal AI assistants for any kind of domain corpus.

### 🛠️ Troubleshooting
Tesseract not found?
Ensure it's installed and added to your system PATH.

FAISS errors on Windows?
Prefer using faiss-cpu or run in WSL for full compatibility.

Groq key errors?
Double-check the .env key and verify your usage/quota on Groq.

📊 Checking Groq API Usage
As of now, Groq does not provide a public dashboard for token usage like OpenAI. However, you can:

Check limits via email/Groq support.

Track approximate usage manually in the app logs.

Stay tuned for Groq dashboard updates: https://console.groq.com

### 🔮 Future Improvements
 LangChain integration

### Streaming responses

 Highlight matched text in source documents

 UI themes and dark mode

### 🙏 Acknowledgements
Groq

Meta's LLaMA 3

Sentence Transformers

Streamlit

Tesseract OCR

### 📜 License
This project is licensed under the MIT License. Feel free to use, modify, and share it.

### 🤝 Contributing
Pull requests, feedback, and ideas are most welcome!
Just fork the repo, make your changes, and raise a PR.

### 👋 Author
Deepan


---


