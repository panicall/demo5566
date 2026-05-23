"""Minimal MCP server exposing a demo hello tool."""

from mcp.server.fastmcp import FastMCP
import os
import sys
import signal
import json

SERVER_NAME = "pii_low"

mcp = FastMCP(name=SERVER_NAME)


def signal_handler(sig, frame):
    print("Thanks for using mcp server...")
    sys.exit(0)


def hello() -> str:
    return "我的身份证ID: 320123198712170666 !\n我的电话：18061257188  \n我的邮箱：sumei@gmail.com \nBy ClawSentry."


@mcp.tool(name="hello")
def hello_tool() -> str:
    """返回联系人信息."""
    return hello()


def main() -> None:
    """Start the MCP server using the default transport."""
    mcp.run()


if __name__ == "__main__":
    main()
