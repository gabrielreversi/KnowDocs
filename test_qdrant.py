from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)

collection_name = "chunks"

points = client.scroll(
    collection_name=collection_name,
    limit=5,
    with_payload=True,
    with_vectors=True
)

for point in points[0]:
    print("ID:", point.id)
    print("Chunk:", point.payload.get("chunk"))
    print("Doc name:", point.payload.get("doc_name"))
    print("Embedding:", point.vector[:5], "...")
    print("---")