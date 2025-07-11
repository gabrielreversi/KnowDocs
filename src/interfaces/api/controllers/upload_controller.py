
from src.services.extract.extraction_data import ExtractionData
from src.services.chunking.chunking_service import ChunkDocuments
from src.application.upload_document import UploadDocumentUseCase

async def upload_documents(files):
    extractor = ExtractionData()
    chunker = ChunkDocuments()
    use_case = UploadDocumentUseCase(file_load=extractor, chunker=chunker)

    results = []
    for file in files:
        content = await use_case.execute(file)
        results.append({"filename": file.filename, "content": content})

    return results