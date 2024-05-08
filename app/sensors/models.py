from pydantic import BaseModel

class Sensor(BaseModel):
    sensor_id: int
    sensor_name: str
