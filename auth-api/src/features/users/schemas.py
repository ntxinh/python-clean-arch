from pydantic import BaseModel, EmailStr, ConfigDict


# Base properties
class UserBase(BaseModel):
    username: str
    email: EmailStr


# Input for Registration
class UserCreate(UserBase):
    password: str


# Output for API
class UserResponse(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
