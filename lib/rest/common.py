"""
Common utilities for the FHIR MCP server (REST).
"""
from typing import Dict
import requests


class Request:
    headers: Dict[str, str] = {
        "Accept": "application/fhir+{_format};q=1.0, application/{_format}+fhir;q=0.9",
        "User-Agent": "HAPI-FHIR/7.6.0 (FHIR Client; FHIR 4.0.1/R4; apache)",
        "Accept-Encoding": "gzip"
    }

    def __init__(self, host: str, port: int, path: str) -> None:
        """
        Initialize the request with host, port, and path.
        :param host: The host for the request.
        :param port: The port for the request.
        :param path: The path for the request.
        """
        self.host = host
        self.port = port
        self.path = path
    
    def send(self, resource: str, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Send the request.
        :param resource: The resource for the request.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        headers = self.headers.copy()
        
        headers["Accept"] = headers["Accept"].format(_format=_format)

        response = requests.get(f"http://{self.host}:{self.port}{self.path}/{resource}/{_id}/_history/{_version}?_format={_format}&_pretty={_pretty}", headers=headers)
        return response.json()
