from abc import ABC, abstractmethod

class ChunkerText(ABC):
    @abstractmethod
    def chunk(self, text: str) -> list[str]:
        """ Split documents in small parts """
        pass