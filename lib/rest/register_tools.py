"""
Tool registrations for FHIR (REST).
"""
from lib.mcp_init import mcp
from lib.rest.resources import Encounter, Observation, Patient, Procedure, Condition
from settings import FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH

@mcp.tool(tags={"observation", "read"})
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

@mcp.tool(tags={"procedure", "read"})
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

@mcp.tool(tags={"patient", "read"})
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

@mcp.tool(tags={"condition", "read"})
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

@mcp.tool(tags={"encounter", "read"})
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

@mcp.tool(tags={"appointment", "read"})
def get_appointment(_id: str, _version: int, _format: str = 'json', _pretty: bool = True):
    """
    Get an appointment resource.
    :param _id: The ID of the appointment.
    :param _version: The version of the appointment.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    from lib.rest.resources import Appointment
    appointment = Appointment(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return appointment.get_appointment(_id, _version, _format=_format, _pretty=_pretty)

# Latest version read operations
@mcp.tool(tags={"observation", "read"})
def get_observation_latest(_id: str, _format: str = 'json', _pretty: bool = True):
    """
    Get the latest version of an observation resource.
    :param _id: The ID of the observation.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    observation = Observation(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return observation.get_observation_latest(_id, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"procedure", "read"})
def get_procedure_latest(_id: str, _format: str = 'json', _pretty: bool = True):
    """
    Get the latest version of a procedure resource.
    :param _id: The ID of the procedure.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    procedure = Procedure(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return procedure.get_procedure_latest(_id, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"patient", "read"})
def get_patient_latest(_id: str, _format: str = 'json', _pretty: bool = True):
    """
    Get the latest version of a patient resource.
    :param _id: The ID of the patient.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    patient = Patient(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return patient.get_patient_latest(_id, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"condition", "read"})
def get_condition_latest(_id: str, _format: str = 'json', _pretty: bool = True):
    """
    Get the latest version of a condition resource.
    :param _id: The ID of the condition.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    condition = Condition(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return condition.get_condition_latest(_id, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"encounter", "read"})
def get_encounter_latest(_id: str, _format: str = 'json', _pretty: bool = True):
    """
    Get the latest version of an encounter resource.
    :param _id: The ID of the encounter.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    encounter = Encounter(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return encounter.get_encounter_latest(_id, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"appointment", "read"})
def get_appointment_latest(_id: str, _format: str = 'json', _pretty: bool = True):
    """
    Get the latest version of an appointment resource.
    :param _id: The ID of the appointment.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    from lib.rest.resources import Appointment
    appointment = Appointment(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return appointment.get_appointment_latest(_id, _format=_format, _pretty=_pretty)

# Create operations
@mcp.tool(tags={"observation", "create"})
def create_observation(data: dict, _format: str = 'json', _pretty: bool = True):
    """
    Create a new observation resource.
    :param data: The observation data to create.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    observation = Observation(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return observation.create_observation(data, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"procedure", "create"})
def create_procedure(data: dict, _format: str = 'json', _pretty: bool = True):
    """
    Create a new procedure resource.
    :param data: The procedure data to create.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    procedure = Procedure(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return procedure.create_procedure(data, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"patient", "create"})
def create_patient(data: dict, _format: str = 'json', _pretty: bool = True):
    """
    Create a new patient resource.
    :param data: The patient data to create.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    patient = Patient(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return patient.create_patient(data, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"condition", "create"})
def create_condition(data: dict, _format: str = 'json', _pretty: bool = True):
    """
    Create a new condition resource.
    :param data: The condition data to create.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    condition = Condition(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return condition.create_condition(data, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"encounter", "create"})
def create_encounter(data: dict, _format: str = 'json', _pretty: bool = True):
    """
    Create a new encounter resource.
    :param data: The encounter data to create.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    encounter = Encounter(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return encounter.create_encounter(data, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"appointment", "create"})
def create_appointment(data: dict, _format: str = 'json', _pretty: bool = True):
    """
    Create a new appointment resource.
    :param data: The appointment data to create.
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    from lib.rest.resources import Appointment
    appointment = Appointment(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return appointment.create_appointment(data, _format=_format, _pretty=_pretty)

# Update operations
@mcp.tool(tags={"observation", "update"})
def update_observation(_id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
    """
    Update an existing observation resource.
    :param _id: The ID of the observation to update.
    :param data: The updated observation data.
    :param if_match: The ETag for concurrency control (optional).
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    observation = Observation(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return observation.update_observation(_id, data, if_match=if_match, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"procedure", "update"})
def update_procedure(_id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
    """
    Update an existing procedure resource.
    :param _id: The ID of the procedure to update.
    :param data: The updated procedure data.
    :param if_match: The ETag for concurrency control (optional).
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    procedure = Procedure(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return procedure.update_procedure(_id, data, if_match=if_match, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"patient", "update"})
def update_patient(_id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
    """
    Update an existing patient resource.
    :param _id: The ID of the patient to update.
    :param data: The updated patient data.
    :param if_match: The ETag for concurrency control (optional).
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    patient = Patient(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return patient.update_patient(_id, data, if_match=if_match, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"condition", "update"})
def update_condition(_id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
    """
    Update an existing condition resource.
    :param _id: The ID of the condition to update.
    :param data: The updated condition data.
    :param if_match: The ETag for concurrency control (optional).
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    condition = Condition(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return condition.update_condition(_id, data, if_match=if_match, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"encounter", "update"})
def update_encounter(_id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
    """
    Update an existing encounter resource.
    :param _id: The ID of the encounter to update.
    :param data: The updated encounter data.
    :param if_match: The ETag for concurrency control (optional).
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    encounter = Encounter(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return encounter.update_encounter(_id, data, if_match=if_match, _format=_format, _pretty=_pretty)

@mcp.tool(tags={"appointment", "update"})
def update_appointment(_id: str, data: dict, if_match: str = None, _format: str = 'json', _pretty: bool = True):
    """
    Update an existing appointment resource.
    :param _id: The ID of the appointment to update.
    :param data: The updated appointment data.
    :param if_match: The ETag for concurrency control (optional).
    :param _format: The format for the response (default: 'json').
    :param _pretty: Whether to pretty-print the response (default: True).
    """
    from lib.rest.resources import Appointment
    appointment = Appointment(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return appointment.update_appointment(_id, data, if_match=if_match, _format=_format, _pretty=_pretty)

# Delete operations
@mcp.tool(tags={"observation", "delete"})
def delete_observation(_id: str, _format: str = 'json'):
    """
    Delete an observation resource.
    :param _id: The ID of the observation to delete.
    :param _format: The format for the response (default: 'json').
    """
    observation = Observation(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return observation.delete_observation(_id, _format=_format)

@mcp.tool(tags={"procedure", "delete"})
def delete_procedure(_id: str, _format: str = 'json'):
    """
    Delete a procedure resource.
    :param _id: The ID of the procedure to delete.
    :param _format: The format for the response (default: 'json').
    """
    procedure = Procedure(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return procedure.delete_procedure(_id, _format=_format)

@mcp.tool(tags={"patient", "delete"})
def delete_patient(_id: str, _format: str = 'json'):
    """
    Delete a patient resource.
    :param _id: The ID of the patient to delete.
    :param _format: The format for the response (default: 'json').
    """
    patient = Patient(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return patient.delete_patient(_id, _format=_format)

@mcp.tool(tags={"condition", "delete"})
def delete_condition(_id: str, _format: str = 'json'):
    """
    Delete a condition resource.
    :param _id: The ID of the condition to delete.
    :param _format: The format for the response (default: 'json').
    """
    condition = Condition(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return condition.delete_condition(_id, _format=_format)

@mcp.tool(tags={"encounter", "delete"})
def delete_encounter(_id: str, _format: str = 'json'):
    """
    Delete an encounter resource.
    :param _id: The ID of the encounter to delete.
    :param _format: The format for the response (default: 'json').
    """
    encounter = Encounter(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return encounter.delete_encounter(_id, _format=_format)

@mcp.tool(tags={"appointment", "delete"})
def delete_appointment(_id: str, _format: str = 'json'):
    """
    Delete an appointment resource.
    :param _id: The ID of the appointment to delete.
    :param _format: The format for the response (default: 'json').
    """
    from lib.rest.resources import Appointment
    appointment = Appointment(FHIR_REST_HOST, FHIR_REST_PORT, FHIR_REST_PATH)
    return appointment.delete_appointment(_id, _format=_format)
