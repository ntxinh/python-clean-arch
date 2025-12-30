from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.shared.database import get_db
from src.features.users import service, schemas

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=schemas.UserResponse)
async def register(user_in: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    return await service.register_user(db, user_in)
