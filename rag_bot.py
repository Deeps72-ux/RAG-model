from transformers import pipeline
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load context
with open("data/context.txt", "r") as f:
    docs = f.read().split("\n\n")  # split by paragraph

# Step 1: Encode documents using Sentence Transformer
embedder = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = embedder.encode(docs, convert_to_numpy=True)

# Step 2: Index using FAISS
dimension = doc_embeddings.shape[1]
print("The dimension of each vector is ",dimension)
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

# Step 3: Load local text-to-text generator (FLAN-T5)
generator = pipeline("text2text-generation", model="google/flan-t5-base")

print("🔍 RAG chatbot ready! Type your questions. type exit or quit to leave\n")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break

    # Step 4: Embed the query
    query_embedding = embedder.encode([query], convert_to_numpy=True)

    # Step 5: Retrieve top-3 relevant docs
    k = 3
    distances, indices = index.search(query_embedding, k)
    retrieved = "\n".join([docs[i] for i in indices[0]])

    # Step 6: Construct prompt and generate answer
    prompt = f"Answer the question: {query}\nContext: {retrieved}"
    answer = generator(prompt, max_length=128, do_sample=True)[0]['generated_text']

    print(f"Bot: {answer}\n")
