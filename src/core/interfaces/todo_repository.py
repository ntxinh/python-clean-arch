from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.domain.todo import Todo

class TodoRepository(ABC):
    @abstractmethod
    async def create(self, todo: Todo) -> Todo:
        pass

    @abstractmethod
    async def get_by_id(self, todo_id: int) -> Optional[Todo]:
        pass

    @abstractmethod
    async def list(self, limit: int, offset: int, title_search: Optional[str]) -> List[Todo]:
        pass

    @abstractmethod
    async def update(self, todo: Todo) -> Todo:
        pass

    @abstractmethod
    async def delete(self, todo_id: int) -> bool:
        pass