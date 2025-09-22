"""
Appointment model.

{
  "resourceType" : "Appointment",
  "id" : "example",
  "text" : {
    "status" : "generated",
    "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">Brian MRI results discussion</div>"
  },
  "status" : "booked",
  "class" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-ActCode",
      "code" : "AMB",
      "display" : "ambulatory"
    }]
  }],
  "serviceCategory" : [{
    "coding" : [{
      "system" : "http://example.org/service-category",
      "code" : "gp",
      "display" : "General Practice"
    }]
  }],
  "serviceType" : [{
    "concept" : {
      "coding" : [{
        "code" : "52",
        "display" : "General Discussion"
      }]
    }
  }],
  "specialty" : [{
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "394814009",
      "display" : "General practice"
    }]
  }],
  "appointmentType" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v2-0276",
      "code" : "FOLLOWUP",
      "display" : "A follow up visit from a previous appointment"
    }]
  },
  "reason" : [{
    "reference" : {
      "reference" : "Condition/example",
      "display" : "Severe burn of left ear"
    }
  }],
  "description" : "Discussion on the results of your recent MRI",
  "start" : "2013-12-10T09:00:00Z",
  "end" : "2013-12-10T11:00:00Z",
  "created" : "2013-10-10",
  "note" : [{
    "text" : "Further expand on the results of the MRI and determine the next actions that may be appropriate."
  }],
  "patientInstruction" : [{
    "concept" : {
      "text" : "Please avoid excessive travel (specifically flying) before this appointment"
    }
  }],
  "basedOn" : [{
    "reference" : "ServiceRequest/myringotomy"
  }],
  "subject" : {
    "reference" : "Patient/example",
    "display" : "Peter James Chalmers"
  },
  "participant" : [{
    "actor" : {
      "reference" : "Patient/example",
      "display" : "Peter James Chalmers"
    },
    "required" : true,
    "status" : "accepted"
  },
  {
    "type" : [{
      "coding" : [{
        "system" : "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        "code" : "ATND"
      }]
    }],
    "actor" : {
      "reference" : "Practitioner/example",
      "display" : "Dr Adam Careful"
    },
    "required" : true,
    "status" : "accepted"
  },
  {
    "actor" : {
      "reference" : "Location/1",
      "display" : "South Wing, second floor"
    },
    "required" : true,
    "status" : "accepted"
  }]
}
"""
from typing import Dict

from lib.models.common import FHIRResource, Reference, Actor, Coding


class Appointment(FHIRResource):
    resource_type = "Appointment"

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
    def description(self) -> str:
        return self.data.get("description", "")
    
    @property
    def start(self) -> str:
        return self.data.get("start", "")
    
    @property
    def end(self) -> str:
        return self.data.get("end", "")
    
    @property
    def subject(self) -> Reference:
        subject_data = self.data.get("subject", {})
        return Reference(
            reference=subject_data.get("reference", ""),
            display=subject_data.get("display", "")
        )
    
    @property
    def participants(self) -> list:
        participants_data = self.data.get("participant", [])
        participants = []
        for participant in participants_data:
            actor_data = participant.get("actor", {})
            actor = Actor(
                reference=actor_data.get("reference", ""),
                display=actor_data.get("display", "")
            )
            participants.append({
                "actor": actor,
                "required": participant.get("required", False),
                "status": participant.get("status", "")
            })
        return participants
    
    def to_dict(self) -> Dict:
        return self.data
    
    def __repr__(self) -> str:
        return f"<Appointment id={self.id} status={self.status} start={self.start} end={self.end}>"
    
    def __str__(self) -> str:
        return f"Appointment(id={self.id}, status={self.status}, start={self.start}, end={self.end})"
