"""
FHIR MCP Server Initialization
"""
from fastmcp import Context, FastMCP
from fastmcp.server.middleware.logging import LoggingMiddleware
from fastmcp.server.middleware.timing import TimingMiddleware
from starlette.requests import Request
from starlette.responses import PlainTextResponse

from settings import EXCLUDE_TAGS, INCLUDE_TAGS, logger

def mcp_factory() -> FastMCP[Context]:
    if type(INCLUDE_TAGS) is set and type(EXCLUDE_TAGS) is set:
        return FastMCP("FHIR MCP Server", include_tags=INCLUDE_TAGS, exclude_tags=EXCLUDE_TAGS)
    elif type(INCLUDE_TAGS) is set:
        return FastMCP("FHIR MCP Server", include_tags=INCLUDE_TAGS)
    elif type(EXCLUDE_TAGS) is set:
        return FastMCP("FHIR MCP Server", exclude_tags=EXCLUDE_TAGS)
    else:
        return FastMCP("FHIR MCP Server")

mcp: FastMCP[Context] = mcp_factory()

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

