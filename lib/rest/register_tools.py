"""
Tool registrations for FHIR (REST).
"""
from lib.mcp_init import mcp
from lib.rest.resources import Encounter, Observation, Patient, Procedure, Condition
from settings import FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH

@mcp.tool
def get_observation(_id: str, _version: int, _format: str = 'json', _pretty: bool = True):
    """
    Get an observation resource.
    :param _id: The ID of the observation.
    :param _version: The version of the observation.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    observation = Observation(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return observation.get_observation(_id, _version, _format=_format, _pretty=_pretty)

@mcp.tool
def get_procedure(_id: str, _version: int, _format: str = 'json', _pretty: bool = True):
    """
    Get a procedure resource.
    :param _id: The ID of the procedure.
    :param _version: The version of the procedure.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    procedure = Procedure(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return procedure.get_procedure(_id, _version, _format=_format, _pretty=_pretty)

@mcp.tool
def get_patient(_id: str, _version: int, _format: str = 'json', _pretty: bool = True):
    """
    Get a patient resource.
    :param _id: The ID of the patient.
    :param _version: The version of the patient.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    patient = Patient(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return patient.get_patient(_id, _version, _format=_format, _pretty=_pretty)

@mcp.tool
def get_condition(_id: str, _version: int, _format: str = 'json', _pretty: bool = True):
    """
    Get a condition resource.
    :param _id: The ID of the condition.
    :param _version: The version of the condition.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    condition = Condition(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return condition.get_condition(_id, _version, _format=_format, _pretty=_pretty)

@mcp.tool
def get_encounter(_id: str, _version: int, _format: str = 'json', _pretty: bool = True):
    """
    Get an encounter resource.
    :param _id: The ID of the encounter.
    :param _version: The version of the encounter.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    encounter = Encounter(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return encounter.get_encounter(_id, _version, _format=_format, _pretty=_pretty)
