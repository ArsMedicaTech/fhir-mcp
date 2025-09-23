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

    def send_latest(self, resource: str, _id: str, _format: str = 'json', _pretty: bool = True):
        """
        Send a request to get the latest version of a resource.
        :param resource: The resource for the request.
        :param _id: The ID of the resource.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        headers = self.headers.copy()
        headers["Accept"] = headers["Accept"].format(_format=_format)

        response = requests.get(f"http://{self.host}:{self.port}{self.path}/{resource}/{_id}?_format={_format}&_pretty={_pretty}", headers=headers)
        return response.json()

    def create(self, resource: str, data: dict, _format: str = 'json', _pretty: bool = True):
        """
        Create a new resource.
        :param resource: The resource type to create.
        :param data: The resource data to create.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        headers = self.headers.copy()
        headers["Content-Type"] = f"application/fhir+{_format}"
        headers["Accept"] = headers["Accept"].format(_format=_format)

        response = requests.post(f"http://{self.host}:{self.port}{self.path}/{resource}?_format={_format}&_pretty={_pretty}", 
                               json=data, headers=headers)
        return response.json()

    def update(self, resource: str, _id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
        """
        Update an existing resource.
        :param resource: The resource type to update.
        :param _id: The ID of the resource to update.
        :param data: The updated resource data.
        :param if_match: The ETag for concurrency control (optional).
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        headers = self.headers.copy()
        headers["Content-Type"] = f"application/fhir+{_format}"
        headers["Accept"] = headers["Accept"].format(_format=_format)
        
        if if_match:
            headers["If-Match"] = if_match

        response = requests.put(f"http://{self.host}:{self.port}{self.path}/{resource}/{_id}?_format={_format}&_pretty={_pretty}", 
                              json=data, headers=headers)
        return response.json()

    def delete(self, resource: str, _id: str, _format: str = 'json'):
        """
        Delete a resource.
        :param resource: The resource type to delete.
        :param _id: The ID of the resource to delete.
        :param _format: The format for the response (default: 'json').
        """
        headers = self.headers.copy()
        headers["Accept"] = headers["Accept"].format(_format=_format)

        response = requests.delete(f"http://{self.host}:{self.port}{self.path}/{resource}/{_id}?_format={_format}", 
                                 headers=headers)
        return response.json() if response.content else {"status": response.status_code}
