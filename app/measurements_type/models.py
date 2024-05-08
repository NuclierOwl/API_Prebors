from pydantic import BaseModel

class MeasurementType(BaseModel):
    type_id: int
    type_name: str
    type_units: str

class MeasurementTypeCreate(BaseModel):
    type_name: str
    type_units: str

class MeasurementTypeUpdate(BaseModel):
    type_name: str
    type_units: str
