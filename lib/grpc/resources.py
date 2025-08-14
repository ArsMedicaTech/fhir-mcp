"""
gRPC utilities for FHIR resources.
"""
from typing import Optional
from arsmedicatech.fhir_sync_pb2 import PatientRef
from arsmedicatech.fhir_sync_pb2_grpc import FhirSyncStub
from google.fhir.proto.r5.core.resources import patient_pb2
from lib.grpc.common import GRPCController


class Patient(GRPCController):
    def __init__(
        self,
        address: str = "localhost:50051",
        secure: bool = False,
        cert_path: Optional[str] = None,
    ):
        super().__init__(FhirSyncStub, address, secure, cert_path)

    def get_patient(self, patient_id: str):
        request = PatientRef(id=patient_id)
        return self.call("GetPatient", request)
