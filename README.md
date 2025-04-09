# 📚 RAG Chatbot 🔍 🤖 — Powered by LLaMA 3

Welcome to **Deepan's RAG Chatbot**, a lightweight, efficient Retrieval-Augmented Generation (RAG) chatbot that supports **PDF**, **text**, and **image (OCR: Optical Character Recognition)** uploads.
 This app uses the power of **LLaMA 3 hosted via Groq API**, **FAISS** for vector search, and **Sentence Transformers** for document embeddings.

![banner](https://img.shields.io/badge/Powered%20By-Groq%20%2B%20LLaMA3-brightgreen)  
🔗 Hosted on GitHub: [Deeps72-ux/RAG-model](https://github.com/Deeps72-ux/RAG-model)

---

## 🚀 Features

- 📁 Upload and process multiple file types: `.txt`, `.pdf`, `.jpg`, `.jpeg`
- 🔍 OCR support using Tesseract for image files
- 🧠 Embed documents using `all-MiniLM-L6-v2` from Sentence Transformers
- 📚 FAISS vector store for fast semantic search
- 💬 Interactive Streamlit chat interface with chat history memory 
- 🤖 Contextual responses generated via **Groq-hosted LLaMA 3 (8B)**
  
---

## 🧰 Tech Stack

| Component       | Library/Tool                             |
|-----------------|-------------------------------------------|
| User Interface  | Streamlit                                |
| Embeddings      | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector database   | FAISS                                     |
| OCR             | PyTesseract                               |
| PDF Reading     | PyPDF2                                    |
| LLM             | Groq API (LLaMA 3)                        |
| Image Handling  | Pillow (`PIL`)                            |
| API Secrets     | dotenv (`.env` file for config)           |

- **For text processing:** nltk library was used

---

## 📁 File Structure
RAG-model/ <br>
├── final_RAG_model.py # Main Streamlit application  <br>
├── requirements.txt <br>
├── .env # Groq API key (excluded from Git) <br>
└── README.md <br>
└── Construction # consists of different modular units to build the final model

---

## 🧪 How It Works

1. **Document Upload**  
   Upload `.pdf`, `.txt`, or image files (`.jpg`, `.jpeg`).
   The document uploaded by the user gives the context for the LLM (Large Language Model) to process the user queries
   
3. **Text Extraction**  
   - Text files are parsed directly.
   - PDF files are parsed with the help of PyPDF2 library
   - Images use Tesseract OCR to extract text.

4. **Embedding**  
   The text extracted is broken down into a list of sentences and converted into a vector notation (process called as embedding).
   The documents are embedded using `all-MiniLM-L6-v2` via `sentence-transformers` and stored in the faiss (Facebook AI Similarity Search) vector database.

6. **FAISS Indexing**  
   Embeddings are indexed using `faiss.IndexFlatL2`.

7. **Retrieval and generation**  
   For each user query:
   - The top-3 relevant chunks of text are retrieved from the FAISS vector database. They are found using the euclidean distance similarity i.e. the three vectors nearby the query vector in the FAISS database
   - Feed the query to the LLM (Large Language Model) along with the retrieved text as context
   - Display the result of the LLM
  <pre> 
            ┌──────────────┐
            │ Context Doc  │
            └──────┬───────┘
                   ↓
     ┌────────────────────────────┐ 
     │   Sentence Transformer     │
     └────────────┬───────────────┘
                  ↓
            ┌──────────────┐
            │   FAISS DB   │◄─────------------ User Query
            └─────┬────────┘                     │
                  ↓ Top-k Relevant Context       │
        ┌──────────────────────────┐             │
        │    Prompt Generator      │◄─────-------┘
        │   (FLAN-T5 / LLaMA-3)    │
        └────────────┬─────────────┘
                     ↓
               ✨ Final Answer ✨
 </pre>


---


### 📝 Setup Instructions

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
```
macOS:

``` bash
brew install tesseract
```
Windows: Download and install from: https://github.com/tesseract-ocr/tesseract/wiki

### 5. Run the application
``` bash
streamlit run final_RAG_model.py
```

### 🔐 Environment Variables
Create a .env file in the root of your project:

```base
GROQ_API_KEY=your_groq_api_key_here
```

⚠️ The file .env is ignored in this repository on accounts of privacy

### ▶️ Running the App
``` bash
streamlit run app.py
```
The page opens with:

```bash
Deepan's 🙂  RAG Chatbot 🔍 🤖 
📎 Upload files and ask questions with real context!
```

### 💡 Sample Workflow
Upload one or more .txt, .pdf, or .jpg files.

You will see the text generated format which you can edit. 
If you generated text is ok, click "📚 Process Files" to embed them using Sentence Transformers.

Ask any question in the chat box.

Get a concise and relevant answer generated with RAG + Groq's LLaMA 3.

Clear Chat: Option to clear the chat history.

### 🧪 Example Use Cases
Use the RAG model to understand your academic PDFs or scanned notes.

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


