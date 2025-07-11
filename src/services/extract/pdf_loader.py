
import pymupdf4llm
import tempfile

from src.domain.repositories.file_loader import FileLoader


class PDFLoader(FileLoader):

    def __init__(self):
        self.llama_loader = pymupdf4llm.LlamaMarkdownReader()

    async def extract(self, pdf_file):
        text=""
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(pdf_file.file.read())
                tmp_path = tmp.name

                md_text = self.llama_loader.load_data(tmp_path)

                for page in md_text:
                    if page.text_resource is not None:
                        text+=page.text_resource.text + "\n"                   
            return text
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
