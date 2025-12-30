from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.config import settings
from src.shared.database import engine, Base
from src.shared.logger import setup_logging
from src.features.users.router import router as users_router
from src.features.auth.router import router as auth_router

# Lifecycle manager (startup/shutdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Init logs and DB tables
    setup_logging()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown: Close DB connection
    await engine.dispose()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)

# Register Routers
app.include_router(auth_router, prefix=settings.API_PREFIX)
app.include_router(users_router, prefix=settings.API_PREFIX)

@app.get("/health")
def health_check():
    return {"status": "ok", "version": settings.VERSION}