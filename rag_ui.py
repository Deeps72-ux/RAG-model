import streamlit as st
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import PyPDF2
from PIL import Image
import pytesseract
import os
import tempfile

st.set_page_config(page_title="📚 RAG Chatbot", layout="wide")

st.title("🔍 Deepan's RAG Chatbot welcomes you :)")
st.markdown("Kindly upload text, PDF, or image files to provide a background context")

# Globals
embedder = SentenceTransformer("all-MiniLM-L6-v2")
generator = pipeline("question-answering", model="deepset/roberta-base-squad2")
#generator = pipeline("text2text-generation", model="google/flan-t5-base")

docs = []
index = None

# Session states
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "docs" not in st.session_state:
    st.session_state.docs = []

if "index" not in st.session_state:
    st.session_state.index = None

# ----------- File Upload & Preview -----------

uploaded_files = st.file_uploader(
    "📎 Upload multiple files (txt, pdf, jpg/jpeg)", type=["txt", "pdf", "jpg", "jpeg"], accept_multiple_files=True
)

def extract_text(file):
    extension = file.name.split(".")[-1].lower()
    if extension == "txt":
        return file.read().decode("utf-8")
    elif extension == "pdf":
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif extension in ["jpg", "jpeg"]:
        img = Image.open(file)
        return pytesseract.image_to_string(img)
    else:
        return ""

if uploaded_files:
    st.subheader("📄 File Preview")
    extracted_docs = []
    for file in uploaded_files:
        st.markdown(f"**{file.name}**")
        text = extract_text(file)
        #preview = text[:500] + "..." if len(text) > 500 else text
        st.code(text)
        extracted_docs.append(text)

    if st.button("📚 Process Files"):
        with st.spinner("Embedding documents..."):
            st.session_state.docs =sum([doc.split("\n\n") for doc in extracted_docs], [])
            doc_embeddings = embedder.encode(st.session_state.docs, convert_to_numpy=True)

            dim = doc_embeddings.shape[1]
            idx = faiss.IndexFlatL2(dim)
            idx.add(doc_embeddings)

            st.session_state.index = idx
        st.success("Documents indexed and ready to chat!")

# ----------- Chat UI -----------

st.markdown("---")
st.subheader("💬 Chat with your documents : Deepan gives no guarentee for right answer :P")

for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(chat["question"])
    with st.chat_message("assistant"):
        st.markdown(chat["answer"])

user_query = st.chat_input("Ask something...")

if user_query:
    if not st.session_state.index or not st.session_state.docs:
        st.warning("⚠️ Please upload and process documents first.")
    else:
        query_embedding = embedder.encode([user_query], convert_to_numpy=True)
        distances, indices = st.session_state.index.search(query_embedding, k=3)
        retrieved = "\n".join([st.session_state.docs[i] for i in indices[0]])

        prompt = f"Answer the question: {user_query}\n with the following Context: {retrieved}"
        #answer = generator(prompt, max_length=128, do_sample=True)[0]['generated_text']
        answer = generator(question=user_query,context=retrieved)['answer']

        st.session_state.chat_history.append({
            "question": user_query,
            "answer": answer
        })

        with st.chat_message("user"):
            st.markdown(user_query)
        with st.chat_message("assistant"):
            st.markdown(answer)

# ----------- Reset Button -----------

if st.button("🧼 Clear Chat"):
    st.session_state.chat_history = []
    st.success("Chat history cleared.")