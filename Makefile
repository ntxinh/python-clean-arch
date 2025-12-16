.PHONY: help install run clean test fmt

# Default target: show help
help:
	@echo "Usage:"
	@echo "  make install   Install dependencies using uv"
	@echo "  make run       Run the FastAPI server"
	@echo "  make clean     Remove cache files and database"
	@echo "  make test      Run tests (requires pytest)"
	@echo "  make fmt       Format code (requires ruff)"

# Install dependencies
install:
	uv sync

# Run the application
run:
	uv run uvicorn src.main:app --reload --host 127.0.0.1 --port 8000

# Clean up pycache and SQLite DB
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f clean_todo.db

# Run tests (Optional)
test:
	uv run pytest

# Format code (Optional)
fmt:
	uv run ruff format .

# Docker commands
docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f