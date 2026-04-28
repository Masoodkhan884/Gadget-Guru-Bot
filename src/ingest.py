import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

# -----------------------------
# LOAD ENV VARIABLES
# -----------------------------
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

INDEX_NAME = "gadget-guru-bot"

# -----------------------------
# EMBEDDING MODEL
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")  # 384-dim embeddings

# -----------------------------
# INIT PINECONE
# -----------------------------
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create index if it does not exist
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(INDEX_NAME)

# -----------------------------
# LOAD DOCUMENT
# -----------------------------
def load_document(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# -----------------------------
# CHUNKING FUNCTION
# -----------------------------
def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

# -----------------------------
# STORE IN PINECONE
# -----------------------------
def upsert_chunks(chunks):
    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk).tolist()

        index.upsert([
            (
                f"chunk-{i}",
                embedding,
                {"text": chunk}
            )
        ])

    print(f"✅ Stored {len(chunks)} chunks in Pinecone")

# -----------------------------
# MAIN FUNCTION
# -----------------------------
if __name__ == "__main__":

    FILE_PATH = "data/product_specs.txt"

    print("📥 Loading document...")
    text = load_document(FILE_PATH)

    print("✂️ Splitting into chunks...")
    chunks = chunk_text(text)

    print(f"🔢 Total chunks: {len(chunks)}")

    print("🚀 Uploading to Pinecone...")
    upsert_chunks(chunks)

    print("🎉 Ingestion completed successfully!")