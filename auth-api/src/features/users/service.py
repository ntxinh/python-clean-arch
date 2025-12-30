from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
from src.shared.security import get_password_hash
from src.features.users import repository
from src.features.users.schemas import UserCreate


async def register_user(db: AsyncSession, user_in: UserCreate):
    # Check if user exists
    if await repository.get_user_by_username(db, user_in.username):
        logger.warning(
            f"Registration failed: Username {user_in.username} already taken."
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    # Hash password
    hashed_pw = get_password_hash(user_in.password)

    # Create user
    new_user = await repository.create_user(db, user_in, hashed_pw)
    logger.info(f"New user registered: {new_user.id} - {new_user.username}")

    return new_user
