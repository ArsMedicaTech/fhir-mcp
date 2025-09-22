"""
Common models used across the application.
"""


from typing import Dict, List, Optional


class FHIRResource:
    resource_type: str

class Coding:
    def __init__(self, system: str, code: str, display: str):
        self.system = system
        self.code = code
        self.display = display

class Reference:
    def __init__(self, reference: str, display: str):
        self.reference = reference
        self.display = display

class Actor:
    def __init__(self, reference: str, display: str):
        self.reference = reference
        self.display = display


class Identifier:
    def __init__(self, data: Dict):
        self.data = data

    @property
    def use(self) -> str:
        return self.data.get("use", "")
    
    @property
    def type(self) -> Optional[Dict]:
        return self.data.get("type", None)
    
    @property
    def system(self) -> str:
        return self.data.get("system", "")
    
    @property
    def value(self) -> str:
        return self.data.get("value", "")
    
    @property
    def period(self) -> Optional[Dict]:
        return self.data.get("period", None)
    
    @property
    def assigner(self) -> Optional[Dict]:
        return self.data.get("assigner", None)


class Address:
    def __init__(self, data: Dict):
        self.data = data

    @property
    def use(self) -> str:
        return self.data.get("use", "")
    
    @property
    def type(self) -> str:
        return self.data.get("type", "")
    
    @property
    def text(self) -> str:
        return self.data.get("text", "")
    
    @property
    def line(self) -> List[str]:
        return self.data.get("line", [])
    
    @property
    def city(self) -> str:
        return self.data.get("city", "")
    
    @property
    def district(self) -> str:
        return self.data.get("district", "")
    
    @property
    def state(self) -> str:
        return self.data.get("state", "")
    
    @property
    def postal_code(self) -> str:
        return self.data.get("postalCode", "")
    
    @property
    def period(self) -> Optional[Dict]:
        return self.data.get("period", None)



class Contact:
    def __init__(self, data: Dict):
        self.data = data

    @property
    def relationship(self) -> List[Coding]:
        relationships = []
        for rel in self.data.get("relationship", []):
            for coding in rel.get("coding", []):
                relationships.append(
                    Coding(
                        system=coding.get("system", ""),
                        code=coding.get("code", ""),
                        display=coding.get("display", "")
                    )
                )
        return relationships

    @property
    def name(self) -> Optional[Dict]:
        return self.data.get("name", None)

    @property
    def telecom(self) -> List[Dict]:
        return self.data.get("telecom", [])

    @property
    def address(self) -> Optional[Dict]:
        return self.data.get("address", None)

    @property
    def _communication(self) -> List[Dict]:
        return self.data.get("communication", [])



class Name:
    def __init__(self, data: Dict):
        self.data = data

    @property
    def use(self) -> str:
        return self.data.get("use", "")
    
    @property
    def family(self) -> str:
        return self.data.get("family", "")
    
    @property
    def given(self) -> List[str]:
        return self.data.get("given", [])



class ValueQuantity:
    def __init__(self, data: Dict):
        self.data = data

    @property
    def value(self) -> Optional[float]:
        return self.data.get("value", None)

    @property
    def unit(self) -> str:
        return self.data.get("unit", "")

    @property
    def system(self) -> str:
        return self.data.get("system", "")

    @property
    def code(self) -> str:
        return self.data.get("code", "")
