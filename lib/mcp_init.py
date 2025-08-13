"""
FHIR MCP Server Initialization
"""
from fastmcp import Context, FastMCP
from fastmcp.server.middleware.logging import LoggingMiddleware
from fastmcp.server.middleware.timing import TimingMiddleware
from starlette.requests import Request
from starlette.responses import PlainTextResponse

from settings import logger

mcp: FastMCP[Context] = FastMCP("FHIR MCP Server")

# plug‑in generic middleware
mcp.add_middleware(TimingMiddleware())
mcp.add_middleware(LoggingMiddleware())


@mcp.custom_route("/health", methods=["GET"])  # type: ignore[misc]
async def health_check(request: Request) -> PlainTextResponse:
    """
    Health check endpoint to verify server status.
    :param request: Request object containing client information.
    :return: PlainTextResponse indicating server health.
    """
    client_host: str = "unknown"
    if request.client is not None:
        client_host = request.client.host
    logger.debug(f"Health check received from {client_host}")
    logger.debug(str(request.__dir__()))
    return PlainTextResponse("OK")

