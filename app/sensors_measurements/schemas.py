from pydantic import BaseModel
from typing import List

class SensorMeasurement(BaseModel):
    sensor_id: int
    type_id: int
    measurement_formula: str

class SensorMeasurementCreate(BaseModel):
    sensor_id: int
    type_id: int
    measurement_formula: str

class SensorMeasurementList(BaseModel):
    measurements: List[SensorMeasurement]
