# Use the specific version requested
FROM python:3.14.2-slim

# Set environment variables
# PYTHONUNBUFFERED=1: Ensures logs are piped to Docker console immediately
# UV_SYSTEM_PYTHON=1: Tells uv to install packages into the system python (no venv needed in container)
ENV PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

# Install uv (using the official installer)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Copy dependency definition files first (for caching layers)
COPY pyproject.toml uv.lock ./

# Install dependencies
# --frozen: ensures we use exact versions from uv.lock
# --no-dev: skips development dependencies (like pytest/ruff) for production
RUN uv sync --frozen --no-dev

# Copy the rest of the application
COPY src/ src/

# Expose the port
EXPOSE 8000

# Run the application
# Note: Host must be 0.0.0.0 to be accessible outside the container
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]