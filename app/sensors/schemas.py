from pydantic import BaseModel

class SensorBase(BaseModel):
    sensor_name: str

class SensorCreate(SensorBase):
    sensor_id: int

class SensorUpdate(SensorBase):
    pass

class Sensor(SensorBase):
    sensor_id: int

    class Config:
        from_attributes = True
