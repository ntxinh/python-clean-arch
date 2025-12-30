from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_PREFIX}/auth/token")


def verify_password(plain_password, hashed_password):
    # We must also truncate the plain password during verification
    # so it matches the hash logic.
    return pwd_context.verify(plain_password[:72], hashed_password)


def get_password_hash(password):
    # --- DEBUG START ---
    print(f"DEBUG: Type: {type(password)}")
    print(f"DEBUG: Length: {len(str(password))}")
    print(f"DEBUG: Value: {password!r}")  # !r prints the raw representation
    # --- DEBUG END ---
    # Bcrypt max length is 72 bytes.
    # We truncate to 72 characters to prevent the ValueError.
    return pwd_context.hash(password[:72])


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
