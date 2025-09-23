""""""

import json
import os
from os.path import dirname, join
from typing import Optional, Set
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


FHIR_REST_HOST: str = os.getenv("FHIR_REST_HOST", "localhost")
FHIR_REST_PORT: int = int(os.getenv("FHIR_REST_PORT", "8080"))
FHIR_REST_PATH: str = os.getenv("FHIR_REST_PATH", "/fhir")

FHIR_GRPC_HOST: str = os.getenv("FHIR_GRPC_HOST", "fhir.arsmedicatech.com")
FHIR_GRPC_PORT: int = int(os.getenv("FHIR_GRPC_PORT", "443"))

def get_env_var_as_set(var_name: str) -> Optional[Set]:
    """
    Gets an environment variable that is a JSON-encoded list and returns it as a set.
    Returns None if the variable is not set or is an empty string.
    """
    value = os.getenv(var_name)
    # This simple check handles both None and ''
    if not value:
        return None
    return set(json.loads(value))

EXCLUDE_TAGS = get_env_var_as_set("EXCLUDE_TAGS_STR")
INCLUDE_TAGS = get_env_var_as_set("INCLUDE_TAGS_STR")

print(f"EXCLUDE_TAGS: {EXCLUDE_TAGS}")
print(f"INCLUDE_TAGS: {INCLUDE_TAGS}")
