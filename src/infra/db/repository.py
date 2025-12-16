from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from src.core.domain.todo import Todo
from src.core.interfaces.todo_repository import TodoRepository
from src.infra.db.models import TodoModel

class SqliteTodoRepository(TodoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    def _to_domain(self, model: TodoModel) -> Todo:
        return Todo(
            id=model.id,
            title=model.title,
            is_completed=model.is_completed,
            created_at=model.created_at
        )

    async def create(self, todo: Todo) -> Todo:
        db_item = TodoModel(
            title=todo.title, 
            is_completed=todo.is_completed, 
            created_at=todo.created_at
        )
        self.session.add(db_item)
        await self.session.commit()
        await self.session.refresh(db_item)
        return self._to_domain(db_item)

    async def get_by_id(self, todo_id: int) -> Optional[Todo]:
        result = await self.session.execute(select(TodoModel).where(TodoModel.id == todo_id))
        model = result.scalars().first()
        return self._to_domain(model) if model else None

    async def list(self, limit: int, offset: int, title_search: Optional[str]) -> List[Todo]:
        query = select(TodoModel).offset(offset).limit(limit)
        if title_search:
            query = query.where(TodoModel.title.contains(title_search))
        
        result = await self.session.execute(query)
        return [self._to_domain(model) for model in result.scalars().all()]

    async def update(self, todo: Todo) -> Todo:
        # Typically requires fetching the model and updating fields attached to session
        result = await self.session.execute(select(TodoModel).where(TodoModel.id == todo.id))
        model = result.scalars().first()
        
        model.title = todo.title
        model.is_completed = todo.is_completed
        # created_at usually doesn't change
        
        await self.session.commit()
        await self.session.refresh(model)
        return self._to_domain(model)

    async def delete(self, todo_id: int) -> bool:
        result = await self.session.execute(delete(TodoModel).where(TodoModel.id == todo_id))
        await self.session.commit()
        return result.rowcount > 0