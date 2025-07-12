
import uuid
from fastapi import UploadFile
from src.domain.repositories.file_loader import FileLoader
from src.domain.repositories.chunker import ChunkerText
from src.domain.repositories.chunk_repository import ChunkRepository

class UploadDocumentUseCase:
    def __init__(self, file_load: FileLoader, chunker: ChunkerText, chunk_repo: ChunkRepository):
        self.file_loader=file_load
        self.chunker=chunker
        self.chunk_repo=chunk_repo

    async def execute(self, file: UploadFile):
        text = await self.file_loader.extract(file)
        chunks = self.chunker.chunk(text)
        doc_id=str(uuid.uuid4())

        await self.chunk_repo.save_chunks(
            doc_id=doc_id,
            doc_name=file.filename,
            chunks=chunks
        )
        return {
            "doc_id": doc_id,
            "doc_name": file.filename,
            "total_chunks": len(chunks)
        }