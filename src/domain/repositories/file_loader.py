from abc import ABC, abstractmethod
from fastapi import UploadFile

class FileLoader(ABC):
    @abstractmethod
    def extract(self, file: UploadFile):
        """ Extract text from file """
        pass