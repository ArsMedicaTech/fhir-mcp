""""""

import os
from os.path import dirname, join
from typing_extensions import Literal
import typing

from dotenv import load_dotenv

from lib.logger import Logger

logger: Logger = Logger()


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

TransportType = Literal["stdio", "http", "sse", "streamable-http"]

MCP_HOST: str = os.getenv("MCP_HOST", "0.0.0.0")

MCP_TRANSPORT_STRING: str = os.getenv("MCP_TRANSPORT", "http")
if MCP_TRANSPORT_STRING not in ["stdio", "http", "sse", "streamable-http"]:
    raise ValueError(f"Invalid MCP_TRANSPORT value: {MCP_TRANSPORT_STRING}")
MCP_TRANSPORT: TransportType = typing.cast(TransportType, MCP_TRANSPORT_STRING)

MCP_PORT: int = int(os.getenv("MCP_PORT", "9000"))
MCP_PATH: str = os.getenv("MCP_PATH", "/mcp")
MCP_LOG_LEVEL: str = os.getenv("MCP_LOG_LEVEL", "debug")
