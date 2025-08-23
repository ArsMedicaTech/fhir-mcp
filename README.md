# fhir_mcp 

Model Context Protocol server for FHIR resources.

Handles REST and gRPC requests.

Currently only implementing `GET` requests for what to me should be pretty obvious reasons when it comes to LLMs, and especially LLMs that are handling medical data.

## MCP (Model Context Protocol)

### Usage

#### Inspector

1. Start a temporary port forward: `kubectl port-forward -n arsmedicatech service/mcp-server 9000:80`.
2. Run the inspector client: `npx @modelcontextprotocol/inspector@0.14.0`.
3. Navigate to the URL. Something like this: http://127.0.0.1:6274/#tools
4. Enter the URL: http://127.0.0.1:9000/mcp.
5. Click "Connect" to view the available tools.
