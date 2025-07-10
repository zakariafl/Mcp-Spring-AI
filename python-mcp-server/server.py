from mcp.server.fastmcp import FastMCP
mcp = FastMCP('Python-MCP-Server')
@mcp.tool()
def get_info_about(name : str) -> str:
    """
    Get Information about a given employee name:
    - First Name
    - Last Name
    - Salary
    - Email
    """
    return {
        "first_name" : name,
        "last_name" : "zakaria",
        "salary":8800,
        "email":"zakaria@gmail.com"
    }
