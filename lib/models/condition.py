"""
Condition model.

{
  "resourceType" : "Condition",
  "id" : "example",
  "text" : {
    "status" : "generated",
    "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">Severe burn of left ear (Date: 24-May 2012)</div>"
  },
  "clinicalStatus" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/condition-clinical",
      "code" : "active"
    }]
  },
  "verificationStatus" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/condition-ver-status",
      "code" : "confirmed"
    }]
  },
  "category" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/condition-category",
      "code" : "encounter-diagnosis",
      "display" : "Encounter Diagnosis"
    },
    {
      "system" : "http://snomed.info/sct",
      "code" : "439401001",
      "display" : "Diagnosis"
    }]
  }],
  "severity" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "24484000",
      "display" : "Severe"
    }]
  },
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "39065001",
      "display" : "Burn of ear"
    }],
    "text" : "Burnt Ear"
  },
  "bodySite" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "49521004",
      "display" : "Left external ear structure"
    }],
    "text" : "Left Ear"
  }],
  "subject" : {
    "reference" : "Patient/example"
  },
  "onsetDateTime" : "2012-05-24"
}
"""

from typing import Dict, List, Optional
from lib.models.common import FHIRResource, Reference, Coding

class Condition(FHIRResource):
    resource_type = "Condition"

    def __init__(self, data: Dict):
        self.validate_data(data)
        self.data = data
    
    def validate_data(self, data: Dict):
        pass

    @property
    def id(self) -> str:
        return self.data.get("id", "")
    
    @property
    def clinical_status(self) -> Optional[Coding]:
        clinical_status_data = self.data.get("clinicalStatus", {}).get("coding", [])
        if clinical_status_data:
            coding = clinical_status_data[0]
            return Coding(
                system=coding.get("system", ""),
                code=coding.get("code", ""),
                display=coding.get("display", "")
            )
        return None
    
    @property
    def verification_status(self) -> Optional[Coding]:
        verification_status_data = self.data.get("verificationStatus", {}).get("coding", [])
        if verification_status_data:
            coding = verification_status_data[0]
            return Coding(
                system=coding.get("system", ""),
                code=coding.get("code", ""),
                display=coding.get("display", "")
            )
        return None
    
    @property
    def category(self) -> List[Coding]:
        category_data = self.data.get("category", [])
        categories = []
        for cat in category_data:
            for coding in cat.get("coding", []):
                categories.append(Coding(
                    system=coding.get("system", ""),
                    code=coding.get("code", ""),
                    display=coding.get("display", "")
                ))
        return categories
    
    @property
    def severity(self) -> Optional[Coding]:
        severity_data = self.data.get("severity", {}).get("coding", [])
        if severity_data:
            coding = severity_data[0]
            return Coding(
                system=coding.get("system", ""),
                code=coding.get("code", ""),
                display=coding.get("display", "")
            )
        return None
    
    @property
    def code(self) -> Optional[Coding]:
        code_data = self.data.get("code", {}).get("coding", [])
        if code_data:
            coding = code_data[0]
            return Coding(
                system=coding.get("system", ""),
                code=coding.get("code", ""),
                display=coding.get("display", "")
            )
        return None
    
    @property
    def body_site(self) -> List[Coding]:
        body_site_data = self.data.get("bodySite", [])
        body_sites = []
        for site in body_site_data:
            for coding in site.get("coding", []):
                body_sites.append(Coding(
                    system=coding.get("system", ""),
                    code=coding.get("code", ""),
                    display=coding.get("display", "")
                ))

        return body_sites
    
    @property
    def subject(self) -> Optional[Reference]:
        subject_data = self.data.get("subject", {})
        if subject_data:
            return Reference(
                reference=subject_data.get("reference", ""),
                display=subject_data.get("display", "")
            )
        return None

    def to_dict(self) -> Dict:
        return self.data
    
    def __repr__(self) -> str:
        return f"Condition(id={self.id}, clinical_status={self.clinical_status}, verification_status={self.verification_status}, code={self.code})"
    
    def __str__(self) -> str:
        return f"Condition(id={self.id}, clinical_status={self.clinical_status}, verification_status={self.verification_status}, code={self.code})"
