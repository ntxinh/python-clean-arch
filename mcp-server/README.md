# Project Initialization

```sh
# 1. Create a new project directory
mkdir python-mcp-todo
cd python-mcp-todo

# 2. Initialize with uv
uv init

# 3. Add dependencies
uv add fastmcp httpx
```

# How to run

```sh
uv venv
source .venv/bin/activate

# uv
uv run fastmcp dev server.py

# pip
# fastmcp dev server.py
```

# Testing MCP server

## Method 1: The MCP Inspector (Best for Debugging)

The MCP Inspector is a web-based UI that runs locally. It lets you browse your tools, input arguments (like your `token`), and execute them to see the raw JSON results.

1. Run the Inspector Using `uv`, run your server in "dev" mode:

```sh
uv run fastmcp dev server.py
```

- Connect

2. Open the UI

- Your terminal will show a URL (usually `http://localhost:6274`). Open this in your browser.

- Tools > List Tools

- You will see a dashboard listing your tools: `get_my_todos`, `create_todo`, etc.

3. Test a Tool

- Click on `create_todo`.

- Arguments:
    + `token`: Paste a real, valid JWT from your Todo App (you might need to log in to your app's UI and inspect network traffic to grab one).
    + `title`: "Test from Inspector"

- Click Run.

- Verify: You should see the success message on the right, and if you check your real Todo App, the item should appear.

## Method 2: Claude Desktop (Best for "Vibe Checking")

## Method 3: Automated Unit Tests (Best for CI/CD)