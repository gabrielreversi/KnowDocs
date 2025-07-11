
from fastapi import UploadFile
from src.domain.repositories.file_loader import FileLoader
from src.domain.repositories.chunker import ChunkerText

class UploadDocumentUseCase:
    def __init__(self, file_load: FileLoader, chunker: ChunkerText):
        self.file_loader=file_load
        self.chunker=chunker

    async def execute(self, file: UploadFile):
        text = await self.file_loader.extract(file)
        chunks = self.chunker.chunk(text)
        return chunks