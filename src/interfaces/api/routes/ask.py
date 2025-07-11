import fastapi
from fastapi import APIRouter, status, HTTPException

router = APIRouter()

@router.post('/question/', status_code=status.HTTP_200_OK)
def user_question():
    pass