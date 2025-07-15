from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

def get_qdrant_client():
    client = QdrantClient(host="localhost", port=6333)
    client.recreate_collection(
        collection_name="chunks",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )
    return client