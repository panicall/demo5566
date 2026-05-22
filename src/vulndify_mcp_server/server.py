"""Minimal MCP server exposing a demo hello tool."""

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
import os
import sys
import signal
import requests
import json

SERVER_NAME = "pii_low"

mcp = FastMCP(name=SERVER_NAME)


class QueryResponse(BaseModel):
    conversation_id: str
    message: str


def signal_handler(sig, frame):
    print("Thanks for using mcp server...")
    sys.exit(0)


def hello() -> str:
    return "hello world 2026! My ID: 320123198712170666"


@mcp.tool(name="hello")
def hello_tool() -> str:
    """Return a fixed string for demonstration."""
    return hello()


def main() -> None:
    """Start the MCP server using the default transport."""
    mcp.run()


if __name__ == "__main__":
    main()
