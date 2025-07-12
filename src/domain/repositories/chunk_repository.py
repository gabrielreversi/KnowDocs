from abc import ABC, abstractmethod

class ChunkRepository(ABC):
    @abstractmethod
    async def save_chunks(
        self,
        doc_id: str,
        doc_name: str,
        chunks: list[str]
    ):
        pass