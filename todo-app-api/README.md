# Project Initialization

```sh
# 1. Create a new project directory
mkdir clean-todo-fastapi
cd clean-todo-fastapi

# 2. Initialize with uv
uv init

# 3. Pin Python version to 3.14.2
# Note: Ensure Python 3.14.2 is available in your environment or via uv's python management
uv python pin 3.14.2

# 4. Add dependencies
# We use SQLAlchemy + aiosqlite for async SQLite support
uv add fastapi uvicorn sqlalchemy aiosqlite pydantic-settings

# 5. Add Dev dependencies
uv add --dev pytest httpx ruff
```

# Directory Structure

```
clean-todo-fastapi/
├── src/
│   ├── core/
│   │   ├── domain/           # Pure entities (No external deps)
│   │   ├── interfaces/       # Abstract repositories (Ports)
│   │   └── use_cases/        # Application business rules
│   ├── infra/
│   │   ├── db/               # SQLite/SQLAlchemy implementation
│   │   └── web/              # FastAPI Routers & Schemas (DTOs)
│   └── main.py               # Composition Root
├── pyproject.toml
└── app_todo.db             # Generated SQLite file
```

# How to run

```sh
# uv run src/main.py

# Run with Uvicorn
uv run uvicorn src.main:app --reload

# Run as a Module
uv run python -m src.main

# Format
uvx ruff format
uv run ruff format

# Test
uv run pytest
```

- Swagger: http://127.0.0.1:8000/docs
- `/api/v1/todos?page=1&size=5&search=buy`

# Taskfile

```sh
# Start the server
task run

# Installs/syncs dependencies.
task install

# Deletes the .db file (fresh start).
task clean

# Shows all available commands.
task --list
```

# Makefile

```sh
# Start the server:
make run

# Install dependencies:
make install

# Reset the database:
make clean
```

# Docker

```sh
docker compose up --build

# Stop the container
docker compose down

# Start it again
docker compose up -d
```