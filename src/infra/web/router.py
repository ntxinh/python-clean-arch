from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.infra.db.setup import get_db
from src.infra.db.repository import SqliteTodoRepository
from src.core.use_cases.todo_service import TodoService
from src.infra.web.schemas import TodoCreateRequest, TodoUpdateRequest, TodoResponse

router = APIRouter()

# Dependency Injection Helper
def get_service(db: AsyncSession = Depends(get_db)) -> TodoService:
    repo = SqliteTodoRepository(db)
    return TodoService(repo)

@router.post("/todos", response_model=TodoResponse)
async def create_todo(
    request: TodoCreateRequest, 
    service: TodoService = Depends(get_service)
):
    return await service.create_todo(request.title)

@router.get("/todos", response_model=List[TodoResponse])
async def read_todos(
    page: int = Query(1, ge=1), 
    size: int = Query(10, ge=1, le=100),
    search: str | None = None,
    service: TodoService = Depends(get_service)
):
    return await service.get_todos(page, size, search)

@router.get("/todos/{todo_id}", response_model=TodoResponse)
async def read_todo(todo_id: int, service: TodoService = Depends(get_service)):
    todo = await service.repo.get_by_id(todo_id) # Using repo directly for simple read
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/todos/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: int, 
    request: TodoUpdateRequest, 
    service: TodoService = Depends(get_service)
):
    updated = await service.update_todo(todo_id, request.title, request.is_completed)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, service: TodoService = Depends(get_service)):
    success = await service.delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"ok": True}