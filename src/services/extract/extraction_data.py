
from src.services.extract.pdf_loader import PDFLoader
from src.services.extract.docx_loader import DOCXLoader
from src.services.extract.ppt_loader import PPTLoader

from src.domain.repositories.file_loader import FileLoader

class ExtractionData(FileLoader):
    def extract(self, file) -> str:
        ext = file.filename.lower().split(".")[-1]
        loader = self._get_loader(ext)
        return loader.extract(file)
    
    def _get_loader(self, ext:str) -> FileLoader:
        try:
            if ext == 'pdf':
                return PDFLoader()
            elif ext == 'docx':
                return DOCXLoader()
            elif ext == 'ppt':
                return PPTLoader()
        except Exception as e:
            raise ValueError(f"Type os file not supported: {ext}")