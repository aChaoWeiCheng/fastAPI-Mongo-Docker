from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)
from .settings import db
router = APIRouter()

@router.get("/")
async def root():
    user = {
        "email":"root@test.com",
        "password":"123",
        "name":"Admin chao"
    }
    
    await db["users"].insert_one(user) 

    return {"Hello":"OK"}