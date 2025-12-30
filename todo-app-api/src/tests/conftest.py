# import pytest
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from src.infra.db.setup import get_db
# from src.infra.db.models import Base
# from src.main import app

# # Use in-memory SQLite for tests
# TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


# @pytest.fixture(name="session")
# async def session_fixture():
#     engine = create_async_engine(TEST_DATABASE_URL, echo=False)
#     async_session = async_sessionmaker(engine, expire_on_commit=False)

#     # Create tables in the in-memory DB
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

#     async with async_session() as session:
#         yield session


# @pytest.fixture(name="client")
# def client_fixture(session: AsyncSession):
#     # Override the 'get_db' dependency to use our in-memory session
#     async def override_get_db():
#         yield session

#     app.dependency_overrides[get_db] = override_get_db

#     from fastapi.testclient import TestClient

#     with TestClient(app) as c:
#         yield c

#     app.dependency_overrides.clear()
