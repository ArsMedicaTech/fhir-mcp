
"""
Resources for FHIR (REST).
"""
from lib.rest.common import Request


class Observation(Request):
    def __init__(self, host: str, port: int, path: str) -> None:
        super().__init__(host, port, path)

    def get_observation(self, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Get an observation resource.
        :param _id: The ID of the observation.
        :param _version: The version of the observation.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send("Observation", _id, _version, _format=_format, _pretty=_pretty)

class Procedure(Request):
    def __init__(self, host: str, port: int, path: str) -> None:
        super().__init__(host, port, path)

    def get_procedure(self, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Get a procedure resource.
        :param _id: The ID of the procedure.
        :param _version: The version of the procedure.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send("Procedure", _id, _version, _format=_format, _pretty=_pretty)

class Patient(Request):
    def __init__(self, host: str, port: int, path: str) -> None:
        super().__init__(host, port, path)

    def get_patient(self, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Get a patient resource.
        :param _id: The ID of the patient.
        :param _version: The version of the patient.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send("Patient", _id, _version, _format=_format, _pretty=_pretty)

class Condition(Request):
    def __init__(self, host: str, port: int, path: str) -> None:
        super().__init__(host, port, path)

    def get_condition(self, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Get a condition resource.
        :param _id: The ID of the condition.
        :param _version: The version of the condition.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send("Condition", _id, _version, _format=_format, _pretty=_pretty)

class Encounter(Request):
    def __init__(self, host: str, port: int, path: str) -> None:
        super().__init__(host, port, path)

    def get_encounter(self, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Get an encounter resource.
        :param _id: The ID of the encounter.
        :param _version: The version of the encounter.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send("Encounter", _id, _version, _format=_format, _pretty=_pretty)

