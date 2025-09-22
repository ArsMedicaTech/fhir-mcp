"""
Procedure model.

{
  "resourceType" : "Procedure",
  "id" : "example",
  "meta" : {
    "versionId" : "1"
  },
  "text" : {
    "status" : "generated",
    "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">Routine Appendectomy</div>"
  },
  "status" : "completed",
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "80146002",
      "display" : "Appendectomy (Procedure)"
    }],
    "text" : "Appendectomy"
  },
  "subject" : {
    "reference" : "Patient/example"
  },
  "occurrenceDateTime" : "2013-04-05",
  "recorder" : {
    "reference" : "Practitioner/example",
    "display" : "Dr Cecil Surgeon"
  },
  "reportedReference" : {
    "reference" : "Practitioner/example",
    "display" : "Dr Cecil Surgeon"
  },
  "performer" : [{
    "actor" : {
      "reference" : "Practitioner/example",
      "display" : "Dr Cecil Surgeon"
    }
  }],
  "reason" : [{
    "concept" : {
      "text" : "Generalized abdominal pain 24 hours. Localized in RIF with rebound and guarding"
    }
  }],
  "followUp" : [{
    "text" : "ROS 5 days  - 2013-04-10"
  }],
  "note" : [{
    "text" : "Routine Appendectomy. Appendix was inflamed and in retro-caecal position"
  }],
  "supportingInfo" : [{
    "reference" : "ImagingStudy/example"
  }]
}
"""

from typing import Dict, List, Optional
from lib.models.common import FHIRResource, Reference, Coding, ValueQuantity

class Procedure(FHIRResource):
    resource_type = "Procedure"

    def __init__(self, data: Dict):
        self.validate_data(data)
        self.data = data
    
    def validate_data(self, data: Dict):
        pass

    @property
    def id(self) -> str:
        return self.data.get("id", "")
    
    @property
    def status(self) -> str:
        return self.data.get("status", "")
    
    @property
    def code(self) -> Dict:
        return self.data.get("code", {})
    
    @property
    def subject(self) -> Optional[Reference]:
        subject_data = self.data.get("subject", {})
        if subject_data:
            return Reference(
                reference=subject_data.get("reference", ""),
                display=subject_data.get("display", "")
            )
        return None
    
    @property
    def occurrenceDateTime(self) -> Optional[str]:
        return self.data.get("occurrenceDateTime", None)
    
    @property
    def recorder(self) -> Optional[Reference]:
        recorder_data = self.data.get("recorder", {})
        if recorder_data:
            return Reference(
                reference=recorder_data.get("reference", ""),
                display=recorder_data.get("display", "")
            )
        return None
    
    @property
    def reportedReference(self) -> Optional[Reference]:
        reported_data = self.data.get("reportedReference", {})
        if reported_data:
            return Reference(
                reference=reported_data.get("reference", ""),
                display=reported_data.get("display", "")
            )
        return None
    
    @property
    def performer(self) -> List[Dict]:
        return self.data.get("performer", [])
    
    @property
    def reason(self) -> List[Dict]:
        return self.data.get("reason", [])
    
    @property
    def followUp(self) -> List[Dict]:
        return self.data.get("followUp", [])
    
    @property
    def note(self) -> List[Dict]:
        return self.data.get("note", [])
    
    @property
    def supportingInfo(self) -> List[Dict]:
        return self.data.get("supportingInfo", [])

    def to_dict(self) -> Dict:
        return self.data
    
    def __repr__(self) -> str:
        return f"<Procedure id={self.id} status={self.status} code={self.code}>"
    
    def __str__(self) -> str:
        return f"Procedure(id={self.id}, status={self.status}, code={self.code})"
