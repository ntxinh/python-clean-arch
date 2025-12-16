from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.infra.db.setup import init_db
from src.infra.web.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB on startup
    await init_db()
    yield

app = FastAPI(
    title="Clean Architecture Todo API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    # Run with: uv run uvicorn src.main:app --reload
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)