"""
Observation model.

{
  "resourceType" : "Observation",
  "id" : "example",
  "text" : {
    "status" : "generated",
    "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: Observation</b><a name=\"example\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource Observation &quot;example&quot; </p></div><p><b>status</b>: <span title=\"   the mandatory quality flags:   \">final</span></p><p><b>category</b>: <span title=\"  category code is A code that classifies the general type of observation being made. This is used for searching, sorting and display purposes. \">Vital Signs <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"http://terminology.hl7.org/5.1.0/CodeSystem-observation-category.html\">Observation Category Codes</a>#vital-signs)</span></span></p><p><b>code</b>: <span title=\"  \n    Observations are often coded in multiple code systems.\n      - LOINC provides codes of varying granularity (though not usefully more specific in this particular case) and more generic LOINCs  can be mapped to more specific codes as shown here\n      - snomed provides a clinically relevant code that is usually less granular than LOINC\n      - the source system provides its own code, which may be less or more granular than LOINC\n    \">Body Weight <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"https://loinc.org/\">LOINC</a>#29463-7; <a href=\"https://loinc.org/\">LOINC</a>#3141-9 &quot;Body weight Measured&quot;; <a href=\"https://browser.ihtsdotools.org/\">SNOMED CT</a>#27113001 &quot;Body weight&quot;; clinical-codes#body-weight)</span></span></p><p><b>subject</b>: <a href=\"patient-example.html\">Patient/example</a> &quot;Peter CHALMERS&quot;</p><p><b>encounter</b>: <a href=\"encounter-example.html\">Encounter/example</a></p><p><b>effective</b>: 2016-03-28</p><p><b>value</b>: <span title=\"   In FHIR, units may be represented twice. Once in the\n    agreed human representation, and once in a coded form.\n    Both is best, since it's not always possible to infer\n    one from the other in code.\n\n    When a computable unit is provided, UCUM (http://unitsofmeasure.org)\n    is always preferred, but it doesn't provide notional units (such as\n    &quot;tablet&quot;), etc. For these, something else is required (e.g. SNOMED CT)\n     \">185 lbs<span style=\"background: LightGoldenRodYellow\"> (Details: UCUM code [lb_av] = 'lb_av')</span></span></p></div>"
  },
  "status" : "final",
  "category" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
      "code" : "vital-signs",
      "display" : "Vital Signs"
    }]
  }],
  "code" : {
    "coding" : [{
      "system" : "http://loinc.org",
      "code" : "29463-7",
      "display" : "Body Weight"
    },
    {
      "system" : "http://loinc.org",
      "code" : "3141-9",
      "display" : "Body weight Measured"
    },
    {
      "system" : "http://snomed.info/sct",
      "code" : "27113001",
      "display" : "Body weight"
    },
    {
      "system" : "http://acme.org/devices/clinical-codes",
      "code" : "body-weight",
      "display" : "Body Weight"
    }]
  },
  "subject" : {
    "reference" : "Patient/example"
  },
  "encounter" : {
    "reference" : "Encounter/example"
  },
  "effectiveDateTime" : "2016-03-28",
  "valueQuantity" : {
    "value" : 185,
    "unit" : "lbs",
    "system" : "http://unitsofmeasure.org",
    "code" : "[lb_av]"
  }
}
"""

from typing import Dict, List, Optional

from lib.models.common import FHIRResource, Reference, Coding, ValueQuantity

class Observation(FHIRResource):
    resource_type = "Observation"

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
    def category(self) -> List[Dict]:
        return self.data.get("category", [])
    
    @property
    def code(self) -> Dict:
        return self.data.get("code", {})
    
    @property
    def subject(self) -> Optional[Reference]:
        subject_data = self.data.get("subject", None)
        if subject_data:
            return Reference(
                reference=subject_data.get("reference", ""),
                display=subject_data.get("display", "")
            )
        return None
    
    @property
    def encounter(self) -> Optional[Reference]:
        encounter_data = self.data.get("encounter", None)
        if encounter_data:
            return Reference(
                reference=encounter_data.get("reference", ""),
                display=encounter_data.get("display", "")
            )
        return None
    
    @property
    def effectiveDateTime(self) -> str:
        return self.data.get("effectiveDateTime", "")
    
    @property
    def valueQuantity(self) -> Optional[ValueQuantity]:
        vq_data = self.data.get("valueQuantity", None)
        if vq_data:
            return ValueQuantity(
                value=vq_data.get("value", 0),
                unit=vq_data.get("unit", ""),
                system=vq_data.get("system", ""),
                code=vq_data.get("code", "")
            )
        return None
    
    def to_dict(self) -> Dict:
        return self.data

    def __repr__(self) -> str:
        return f"<Observation id={self.id} status={self.status} code={self.code}>"
    
    def __str__(self) -> str:
        return f"Observation(id={self.id}, status={self.status}, code={self.code})"
