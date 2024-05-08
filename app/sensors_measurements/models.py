from pydantic import BaseModel

class SensorMeasurement(BaseModel):
    sensor_id: int
    type_id: int
    measurement_formula: str
