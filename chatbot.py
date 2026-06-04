import os
import chromadb
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

# Gemini Setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

gemini_model = genai.GenerativeModel("gemini-2.5-flash")

# Embedding Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB
client = chromadb.PersistentClient(path="./vector_db")

collection = client.get_collection("knowledge_base")

print("AI Chatbot Ready!")
print("Type 'exit' to quit\n")

while True:

    question = input("Ask Question: ")

    if question.lower() == "exit":
        break

    query_embedding = embedding_model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = "\n".join(results["documents"][0])

    prompt = f"""
You are an AI assistant.

Answer ONLY using the information present in the context.

Context:
{context}

Question:
{question}
"""

    response = gemini_model.generate_content(prompt)

    print("\nAnswer:\n")
    print(response.text)

    print("\n" + "=" * 60 + "\n")