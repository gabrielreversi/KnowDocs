from uuid import uuid4
from typing import Any
from src.services.db.mongo_chunk_repository import MongoChunkRepository
from src.services.embeddings.embedding_service import EmbeddingService
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

class IndexerService:
    def __init__(
        self, 
        mongo_repo: MongoChunkRepository,
        qdrant_client: QdrantClient,
        embedding_service: EmbeddingService,
        collection_name: str='chunks'
    ):
        self.mongo = mongo_repo
        self.qdrant = qdrant_client
        self.embedder = embedding_service
        self.collection_name = collection_name

    async def index_all_chunks(self):
        chunks = await self.mongo.get_all_chunks()

        if not chunks:
            return
        
        texts = [chunk["chunk"] for chunk in chunks]
        vectors = self.embedder.embed(texts)

        points = []
        for chunk, vector in zip(chunks, vectors):
            points.append(PointStruct(
                id=str(uuid4()),
                vector=vector,
                payload={
                    "doc_id": chunk["doc_id"],
                    "doc_name": chunk["doc_name"],
                    "chunk_id": chunk["chunk_id"],
                    "upload_date": chunk["upload_date"].isoformat(),
                    "chunk": chunk["chunk"]
                }
            ))

        self.qdrant.upsert(
            collection_name=self.collection_name,
            points=points
        )

        print(f"[✅] {len(points)} chunks indexados no Qdrant.")