from datetime import datetime
from src.services.db.mongo_client import db
from src.domain.repositories.chunk_repository import ChunkRepository

class MongoChunkRepository(ChunkRepository):
    def __init__(self):
        self.collection = db['chunks']

    async def save_chunks(self, doc_id: str, doc_name: str, chunks: list[str]):
        now = datetime.utcnow()
        docs=[
            {
                "doc_id": doc_id,
                "doc_name": doc_name,
                "upload_date": now,
                "chunk_id": i,
                "chunk": chunk_text
            }
            for i, chunk_text in enumerate(chunks)
        ]
        await self.collection.insert_many(docs)

