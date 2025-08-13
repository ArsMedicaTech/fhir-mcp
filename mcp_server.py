"""
FHIR MCP server entry point.
"""
import datetime

from settings import MCP_HOST, MCP_LOG_LEVEL, MCP_PATH, MCP_PORT, MCP_TRANSPORT, logger

from lib.mcp_init import mcp


if __name__ == "__main__":
    ts = datetime.datetime.now().isoformat()
    logger.debug(f"Starting FHIR MCP server at {ts}...")

    mcp.run(transport=MCP_TRANSPORT, host=MCP_HOST, port=MCP_PORT, path=MCP_PATH, log_level=MCP_LOG_LEVEL)
