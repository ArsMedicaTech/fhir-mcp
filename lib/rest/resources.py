
"""
Resources for FHIR (REST).
"""
from lib.rest.common import Request


class Observation(Request):
    def __init__(self, host: str, port: int, path: str) -> None:
        super().__init__(host, port, path)

    def get_observation(self, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Get an observation resource by version.
        :param _id: The ID of the observation.
        :param _version: The version of the observation.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send("Observation", _id, _version, _format=_format, _pretty=_pretty)

    def get_observation_latest(self, _id: str, _format: str = 'json', _pretty: bool = True):
        """
        Get the latest version of an observation resource.
        :param _id: The ID of the observation.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send_latest("Observation", _id, _format=_format, _pretty=_pretty)

    def create_observation(self, data: dict, _format: str = 'json', _pretty: bool = True):
        """
        Create a new observation resource.
        :param data: The observation data to create.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.create("Observation", data, _format=_format, _pretty=_pretty)

    def update_observation(self, _id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
        """
        Update an existing observation resource.
        :param _id: The ID of the observation to update.
        :param data: The updated observation data.
        :param if_match: The ETag for concurrency control (optional).
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.update("Observation", _id, data, if_match=if_match, _format=_format, _pretty=_pretty)

    def delete_observation(self, _id: str, _format: str = 'json'):
        """
        Delete an observation resource.
        :param _id: The ID of the observation to delete.
        :param _format: The format for the response (default: 'json').
        """
        return self.delete("Observation", _id, _format=_format)

class Procedure(Request):
    def __init__(self, host: str, port: int, path: str) -> None:
        super().__init__(host, port, path)

    def get_procedure(self, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Get a procedure resource by version.
        :param _id: The ID of the procedure.
        :param _version: The version of the procedure.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send("Procedure", _id, _version, _format=_format, _pretty=_pretty)

    def get_procedure_latest(self, _id: str, _format: str = 'json', _pretty: bool = True):
        """
        Get the latest version of a procedure resource.
        :param _id: The ID of the procedure.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send_latest("Procedure", _id, _format=_format, _pretty=_pretty)

    def create_procedure(self, data: dict, _format: str = 'json', _pretty: bool = True):
        """
        Create a new procedure resource.
        :param data: The procedure data to create.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.create("Procedure", data, _format=_format, _pretty=_pretty)

    def update_procedure(self, _id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
        """
        Update an existing procedure resource.
        :param _id: The ID of the procedure to update.
        :param data: The updated procedure data.
        :param if_match: The ETag for concurrency control (optional).
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.update("Procedure", _id, data, if_match=if_match, _format=_format, _pretty=_pretty)

    def delete_procedure(self, _id: str, _format: str = 'json'):
        """
        Delete a procedure resource.
        :param _id: The ID of the procedure to delete.
        :param _format: The format for the response (default: 'json').
        """
        return self.delete("Procedure", _id, _format=_format)

class Patient(Request):
    def __init__(self, host: str, port: int, path: str) -> None:
        super().__init__(host, port, path)

    def get_patient(self, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Get a patient resource by version.
        :param _id: The ID of the patient.
        :param _version: The version of the patient.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send("Patient", _id, _version, _format=_format, _pretty=_pretty)

    def get_patient_latest(self, _id: str, _format: str = 'json', _pretty: bool = True):
        """
        Get the latest version of a patient resource.
        :param _id: The ID of the patient.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send_latest("Patient", _id, _format=_format, _pretty=_pretty)

    def create_patient(self, data: dict, _format: str = 'json', _pretty: bool = True):
        """
        Create a new patient resource.
        :param data: The patient data to create.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.create("Patient", data, _format=_format, _pretty=_pretty)

    def update_patient(self, _id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
        """
        Update an existing patient resource.
        :param _id: The ID of the patient to update.
        :param data: The updated patient data.
        :param if_match: The ETag for concurrency control (optional).
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.update("Patient", _id, data, if_match=if_match, _format=_format, _pretty=_pretty)

    def delete_patient(self, _id: str, _format: str = 'json'):
        """
        Delete a patient resource.
        :param _id: The ID of the patient to delete.
        :param _format: The format for the response (default: 'json').
        """
        return self.delete("Patient", _id, _format=_format)

class Condition(Request):
    def __init__(self, host: str, port: int, path: str) -> None:
        super().__init__(host, port, path)

    def get_condition(self, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Get a condition resource by version.
        :param _id: The ID of the condition.
        :param _version: The version of the condition.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send("Condition", _id, _version, _format=_format, _pretty=_pretty)

    def get_condition_latest(self, _id: str, _format: str = 'json', _pretty: bool = True):
        """
        Get the latest version of a condition resource.
        :param _id: The ID of the condition.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send_latest("Condition", _id, _format=_format, _pretty=_pretty)

    def create_condition(self, data: dict, _format: str = 'json', _pretty: bool = True):
        """
        Create a new condition resource.
        :param data: The condition data to create.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.create("Condition", data, _format=_format, _pretty=_pretty)

    def update_condition(self, _id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
        """
        Update an existing condition resource.
        :param _id: The ID of the condition to update.
        :param data: The updated condition data.
        :param if_match: The ETag for concurrency control (optional).
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.update("Condition", _id, data, if_match=if_match, _format=_format, _pretty=_pretty)

    def delete_condition(self, _id: str, _format: str = 'json'):
        """
        Delete a condition resource.
        :param _id: The ID of the condition to delete.
        :param _format: The format for the response (default: 'json').
        """
        return self.delete("Condition", _id, _format=_format)

class Encounter(Request):
    def __init__(self, host: str, port: int, path: str) -> None:
        super().__init__(host, port, path)

    def get_encounter(self, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Get an encounter resource by version.
        :param _id: The ID of the encounter.
        :param _version: The version of the encounter.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send("Encounter", _id, _version, _format=_format, _pretty=_pretty)

    def get_encounter_latest(self, _id: str, _format: str = 'json', _pretty: bool = True):
        """
        Get the latest version of an encounter resource.
        :param _id: The ID of the encounter.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send_latest("Encounter", _id, _format=_format, _pretty=_pretty)

    def create_encounter(self, data: dict, _format: str = 'json', _pretty: bool = True):
        """
        Create a new encounter resource.
        :param data: The encounter data to create.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.create("Encounter", data, _format=_format, _pretty=_pretty)

    def update_encounter(self, _id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
        """
        Update an existing encounter resource.
        :param _id: The ID of the encounter to update.
        :param data: The updated encounter data.
        :param if_match: The ETag for concurrency control (optional).
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.update("Encounter", _id, data, if_match=if_match, _format=_format, _pretty=_pretty)

    def delete_encounter(self, _id: str, _format: str = 'json'):
        """
        Delete an encounter resource.
        :param _id: The ID of the encounter to delete.
        :param _format: The format for the response (default: 'json').
        """
        return self.delete("Encounter", _id, _format=_format)

class Appointment(Request):
    def __init__(self, host: str, port: int, path: str) -> None:
        super().__init__(host, port, path)

    def get_appointment(self, _id: str, _version: int, _format: str = 'json', _pretty: bool = True):
        """
        Get an appointment resource by version.
        :param _id: The ID of the appointment.
        :param _version: The version of the appointment.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send("Appointment", _id, _version, _format=_format, _pretty=_pretty)

    def get_appointment_latest(self, _id: str, _format: str = 'json', _pretty: bool = True):
        """
        Get the latest version of an appointment resource.
        :param _id: The ID of the appointment.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.send_latest("Appointment", _id, _format=_format, _pretty=_pretty)

    def create_appointment(self, data: dict, _format: str = 'json', _pretty: bool = True):
        """
        Create a new appointment resource.
        :param data: The appointment data to create.
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.create("Appointment", data, _format=_format, _pretty=_pretty)

    def update_appointment(self, _id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
        """
        Update an existing appointment resource.
        :param _id: The ID of the appointment to update.
        :param data: The updated appointment data.
        :param if_match: The ETag for concurrency control (optional).
        :param _format: The format for the response (default: 'json').
        :param _pretty: Whether to pretty-print the response (default: True).
        """
        return self.update("Appointment", _id, data, if_match=if_match, _format=_format, _pretty=_pretty)

    def delete_appointment(self, _id: str, _format: str = 'json'):
        """
        Delete an appointment resource.
        :param _id: The ID of the appointment to delete.
        :param _format: The format for the response (default: 'json').
        """
        return self.delete("Appointment", _id, _format=_format)
