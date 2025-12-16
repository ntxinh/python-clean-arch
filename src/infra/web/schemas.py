from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TodoCreateRequest(BaseModel):
    title: str

class TodoUpdateRequest(BaseModel):
    title: Optional[str] = None
    is_completed: Optional[bool] = None

class TodoResponse(BaseModel):
    id: int
    title: str
    is_completed: bool
    created_at: datetime