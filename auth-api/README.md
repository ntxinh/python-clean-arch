```sh
# Create project folder
mkdir my-auth-api
cd my-auth-api

# Initialize python project
uv init

# Add dependencies
uv add fastapi uvicorn pydantic pydantic-settings email-validator
uv add sqlalchemy aiosqlite
uv add "passlib[bcrypt]" "python-jose[cryptography]" python-multipart
uv add python-dotenv loguru

# Lint & Format
uv add --dev ruff

uv run uvicorn src.main:app --port 7000 --reload
```

http://127.0.0.1:7000/docs