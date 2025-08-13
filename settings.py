""""""

import os
from os.path import dirname, join

from dotenv import load_dotenv

from lib.logger import Logger

logger: Logger = Logger()


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


MCP_HOST: str = os.getenv("MCP_HOST", "0.0.0.0")
MCP_TRANSPORT: str = os.getenv("MCP_TRANSPORT", "http")
MCP_PORT: int = int(os.getenv("MCP_PORT", "9000"))
MCP_PATH: str = os.getenv("MCP_PATH", "/mcp")
MCP_LOG_LEVEL: str = os.getenv("MCP_LOG_LEVEL", "debug")
