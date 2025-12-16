from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Todo:
    id: Optional[int]
    title: str
    is_completed: bool
    created_at: datetime