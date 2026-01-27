import httpx
from fastmcp import FastMCP
from pydantic import Field
from typing import Optional, List, Dict, Any

# Initialize the MCP Server
mcp = FastMCP(
    "Todo App Agent"
    # description="An agent that can manage a user's todo list by talking to the REST API."
)

# Configuration: Point this to your existing REST API
API_BASE_URL = "http://127.0.0.1:8000/api/v1"

# --- HELPER FUNCTIONS (Internal) ---
async def _make_request(method: str, endpoint: str, token: str, data: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Internal helper to make secure HTTP calls to your REST API.
    It automatically attaches the User's OAuth Token.
    """
    headers = {
        # "Authorization": f"Bearer {token}",  # <--- CRITICAL: Pass the user's token
        "Content-Type": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method, 
                f"{API_BASE_URL}{endpoint}", 
                headers=headers, 
                json=data,
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            # Return a clear error message that the AI can understand
            return {"error": f"API Error: {e.response.status_code}", "detail": e.response.text}
        except Exception as e:
            return {"error": "Connection Failed", "detail": str(e)}

# --- MCP TOOLS (Public Actions for the AI) ---

@mcp.tool
async def get_my_todos(token: str, status: str = "pending") -> str:
    """
    Fetch the list of todo items for the authenticated user.
    
    Args:
        token: The user's OAuth2 access token.
        status: Filter by status (e.g., 'pending', 'completed').
    """
    search = ''
    data = await _make_request("GET", f"/todos?page=1&size=10&search={search}", token)

    todos = data
    
    # if "error" in data:
    #     return f"Could not fetch todos: {data['detail']}"
    
    # # Format the data nicely for the LLM to read
    # todos = data.get("items", [])
    if not todos:
        return "You have no tasks in this list."
    
    result = [f"- [ID: {t['id']}] {t['title']} ({t['is_completed']})" for t in todos]
    return "\n".join(result)

@mcp.tool
async def create_todo(token: str, title: str, description: str = "") -> str:
    """
    Create a new todo item for the user.
    
    Args:
        token: The user's OAuth2 access token.
        title: The short title of the task.
        description: Additional details about the task.
    """
    payload = {"title": title, "description": description}
    data = await _make_request("POST", "/todos", token, payload)
    
    if "error" in data:
        return f"Failed to create task: {data['detail']}"
        
    return f"Success! Created task #{data['id']}: '{data['title']}'"

@mcp.tool
async def complete_todo(token: str, todo_id: str) -> str:
    """
    Mark a specific todo item as completed.
    
    Args:
        token: The user's OAuth2 access token.
        todo_id: The unique ID of the todo item to complete.
    """
    # First, verify the task exists (Agentic "Think before Act" pattern)
    # This is optional but good practice
    
    # payload = {"status": "completed"}
    payload = { "is_completed": true }
    data = await _make_request("PUT", f"/todos/{todo_id}", token, payload)
    
    if "error" in data:
        return f"Failed to update task: {data['detail']}"
        
    return f"Task #{todo_id} has been marked as completed."

if __name__ == "__main__":
    mcp.run()