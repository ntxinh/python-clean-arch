from pydantic import BaseModel, EmailStr, ConfigDict, Field


# Base properties
class UserBase(BaseModel):
    username: str
    email: EmailStr


# Input for Registration
class UserCreate(UserBase):
    # Enforce max length 72 to align with Bcrypt
    password: str = Field(..., max_length=72, min_length=8)


# Output for API
class UserResponse(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
