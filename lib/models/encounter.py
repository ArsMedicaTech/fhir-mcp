"""
Encounter model.

{
  "resourceType" : "Encounter",
  "id" : "example",
  "text" : {
    "status" : "generated",
    "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">Encounter with patient @example</div>"
  },
  "status" : "in-progress",
  "class" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-ActCode",
      "code" : "IMP",
      "display" : "inpatient encounter"
    }]
  }],
  "subject" : {
    "reference" : "Patient/example"
  },
  "subjectStatus" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/encounter-subject-status",
      "code" : "receiving-care"
    }]
  },
  "careTeam" : [{
    "reference" : "Encounter/example"
  }]
}
"""

from typing import Dict, List, Optional

from lib.models.common import FHIRResource, Reference, Coding

class Encounter(FHIRResource):
    resource_type = "Encounter"

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
    def class_(self) -> List[Dict]:
        return self.data.get("class", [])
    
    @property
    def subject(self) -> Reference:
        subject_data = self.data.get("subject", {})
        return Reference(
            reference=subject_data.get("reference", ""),
            display=subject_data.get("display", "")
        )
    
    @property
    def subject_status(self) -> List[Dict]:
        return self.data.get("subjectStatus", [])
    
    @property
    def care_team(self) -> List[Reference]:
        care_team_data = self.data.get("careTeam", [])
        return [Reference(
            reference=ct.get("reference", ""),
            display=ct.get("display", "")
        ) for ct in care_team_data]

    @property
    def period(self) -> Optional[Dict]:
        return self.data.get("period", None)
