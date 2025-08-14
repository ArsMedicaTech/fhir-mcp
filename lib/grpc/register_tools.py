"""
gRPC tool registrations for FHIR resources.
"""
from google.fhir.proto.r5.core.resources import patient_pb2
from lib.grpc.main import PatientController
from settings import FHIR_GRPC_HOST, FHIR_GRPC_PORT

controller = PatientController(address=f"{FHIR_GRPC_HOST}:{FHIR_GRPC_PORT}", secure=True)
