from typing import List, Optional
from datetime import datetime
from src.core.domain.todo import Todo
from src.core.interfaces.todo_repository import TodoRepository


class TodoService:
    def __init__(self, repo: TodoRepository):
        self.repo = repo

    async def create_todo(self, title: str) -> Todo:
        # Business Logic: New todos are always incomplete and timestamped now
        new_todo = Todo(
            id=None, title=title, is_completed=False, created_at=datetime.now()
        )
        return await self.repo.create(new_todo)

    async def get_todos(
        self, page: int = 1, size: int = 10, search: Optional[str] = None
    ) -> List[Todo]:
        offset = (page - 1) * size
        return await self.repo.list(limit=size, offset=offset, title_search=search)

    async def update_todo(
        self, todo_id: int, title: Optional[str], is_completed: Optional[bool]
    ) -> Optional[Todo]:
        todo = await self.repo.get_by_id(todo_id)
        if not todo:
            return None

        if title is not None:
            todo.title = title
        if is_completed is not None:
            todo.is_completed = is_completed

        return await self.repo.update(todo)

    async def delete_todo(self, todo_id: int) -> bool:
        return await self.repo.delete(todo_id)
