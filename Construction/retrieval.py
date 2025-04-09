from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import nltk
#nltk.download("punkt")
from nltk.tokenize import sent_tokenize

#Load context
with open("../Data/Context.txt","r") as f:
    full_text=f.read() 

#Sentence level split for finer granularity
docs=sent_tokenize(full_text)
print(docs)
print(f"Number of sentences indexed:{len(docs)}")

# Encoding the documents using sentence transformer
embedder = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings=embedder.encode(docs,convert_to_numpy=True)

#Index using FAISS
if docs!=[]:
    dimension=doc_embeddings.shape[1]
    print("The dimension of each vector is ",dimension)
    index=faiss.IndexFlatL2(dimension)
    index.add(doc_embeddings)


while True:
    query=input("You: ")
    if query.lower() in ["exit","quit"]:
        break

    if docs!=[]:
        # Embedding the query
        query_embedding=embedder.encode([query],convert_to_numpy=True)

        #Retriving the top-3 relavent lines from the context
        k = 3
        distances,indices = index.search(query_embedding,k)
        retrieved = "\n".join([docs[i] for i in indices[0]])

        # Constructing prompt, giving the LLM and collecting its answer
        prompt=f"Answer the question:{query}\nContext : {retrieved}"

        print(f"The retrieved content from the text file based on your query : \n {retrieved}\n")
    
    

