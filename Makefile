include .env

# To initialize `.venv`: `python3 -m venv .venv`.

run-mcp:
	.\.venv\Scripts\activate
	python mcp_server.py
