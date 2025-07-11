import fastapi
import tempfile
from src.services.extract.extraction_data import ExtractionData
from src.interfaces.api.controllers.upload_controller import upload_documents
from fastapi import APIRouter, status, HTTPException, UploadFile

router = APIRouter()

@router.post("/upload_file/", status_code=status.HTTP_200_OK)
async def upload_file(pdf_docs: list[UploadFile]):
    return await upload_documents(pdf_docs)

@router.delete("/delete_file/")
async def delete_file():
    pass