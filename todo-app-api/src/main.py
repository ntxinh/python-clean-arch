from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.infra.db.setup import init_db
from src.infra.web.router import router
from src.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB on startup
    await init_db()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)

app.include_router(router, prefix=settings.API_PREFIX)

@app.get("/health")
def health_check():
    return {"status": "ok", "version": settings.VERSION}

if __name__ == "__main__":
    import uvicorn

    # Run with: uv run uvicorn src.main:app --reload
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
