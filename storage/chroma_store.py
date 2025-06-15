import chromadb
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="chapter_versions")

def save_version(version_id: str, text: str, metadata: dict):
    collection.add(
        documents=[text],
        metadatas=[metadata],
        ids=[version_id]
    )
    print(f"✅ Version saved: {version_id}")

def search_versions(query_text: str, n_results=2):
    results = collection.query(query_texts=[query_text], n_results=n_results)
    return results
