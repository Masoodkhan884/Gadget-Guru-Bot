import os
from dotenv import load_dotenv
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# -----------------------------
# LOAD ENV
# -----------------------------
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

INDEX_NAME = "gadget-guru-bot"

# -----------------------------
# EMBEDDING MODEL (SAME AS INGEST)
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# INIT PINECONE
# -----------------------------
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

# -----------------------------
# QUERY FUNCTION
# -----------------------------
def retrieve_context(query, top_k=3):
    """
    Step 1: Convert query to embedding
    Step 2: Search Pinecone
    Step 3: Return top matching texts
    """

    # embed user query
    query_embedding = model.encode(query).tolist()

    # search in pinecone
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    # extract context text
    contexts = []

    for match in results["matches"]:
        text = match["metadata"]["text"]
        score = match["score"]

        contexts.append({
            "text": text,
            "score": score
        })

    return contexts


# -----------------------------
# TEST RUN
# -----------------------------
if __name__ == "__main__":

    question = "How do I reset Bluetooth?"

    print("🔍 Query:", question)

    results = retrieve_context(question)

    print("\n📌 Retrieved Context:\n")

    for i, r in enumerate(results):
        print(f"\n--- Chunk {i+1} (score: {r['score']}) ---")
        print(r["text"])