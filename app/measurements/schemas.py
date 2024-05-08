# app/sensors_measurements/schemas.py

from pydantic import BaseModel


class SensorMeasurementBase(BaseModel):
    sensor_id: int
    type_id: int
    measurement_formula: str


class SensorMeasurementCreate(SensorMeasurementBase):
    pass


class SensorMeasurement(SensorMeasurementBase):
    id: int

    class Config:
        orm_mode = True
