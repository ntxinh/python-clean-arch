from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from src.features.users import repository
from src.shared.security import verify_password, create_access_token
from datetime import timedelta
from src.config import settings


async def authenticate_user(db: AsyncSession, form_data: OAuth2PasswordRequestForm):
    user = await repository.get_user_by_username(db, form_data.username)
    if not user:
        return None
    if not verify_password(form_data.password, user.hashed_password):
        return None
    return user


async def login(db: AsyncSession, form_data: OAuth2PasswordRequestForm):
    user = await authenticate_user(db, form_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
