import asyncio
from src.services.db.mongo_chunk_repository import MongoChunkRepository
from src.services.embeddings.embedding_service import EmbeddingService
from src.services.vector_store.qdrant_client import get_qdrant_client
from src.services.vector_store.indexer_service import IndexerService

async def main():
    mongo_repo = MongoChunkRepository()
    embedder = EmbeddingService()
    qdrant = get_qdrant_client()

    indexer = IndexerService(
        mongo_repo=mongo_repo,
        qdrant_client=qdrant,
        embedding_service=embedder
    )

    await indexer.index_all_chunks()

if __name__ == "__main__":
    asyncio.run(main())