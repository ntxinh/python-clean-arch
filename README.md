# Set up Environment and Run the Debugger

Now, follow these steps in VS Code:

1. Install Python Extension:

If you haven't already, install the official Python extension from Microsoft.

2. Create/Sync your Virtual Environment:

Open a terminal in VS Code and ensure your `auth-api` dependencies are installed and a virtual environment exists. `uv` creates a `.venv` folder by default.

```bash
cd auth-api
uv sync
```

3. Select the Python Interpreter:

- Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
- Type `Python: Select Interpreter`.
- `Enter interpreter path...` or Choose the interpreter located in your project's virtual environment (e.g., `./auth-api/.venv/bin/python`). This is crucial for VS Code to find `uvicorn` and other dependencies.

4. Start Debugging:

- Go to the "Run and Debug" view on the sidebar (or press `Ctrl+Shift+D`).
- Select `"Python: FastAPI (auth-api)"` from the dropdown menu at the top.
- Set a breakpoint in your code (e.g., inside the `health_check` function in `src/main.py`) by clicking in the gutter to the left of the line number.
Press the green "Start Debugging" arrow (or `F5`).

Your FastAPI server will start, and when you access an endpoint (like `http://127.0.0.1:7000/health`), VS Code will pause execution at your breakpoint, allowing you to inspect the state of your application.