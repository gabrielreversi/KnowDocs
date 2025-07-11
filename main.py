
from fastapi import FastAPI
from src.interfaces.api.routes import upload, ask

app = FastAPI()

app.include_router(upload.router, prefix='/Ingestion', tags=['Ingestion'])
app.include_router(ask.router, prefix='/Inference', tags=['Inference'])
