from typing import Optional
from pydantic import BaseModel

class MeasurementBase(BaseModel):
    sensor_inventory_number: Optional[str] = None
    measurement_value: Optional[float] = None
    measurement_ts: Optional[str] = None
    measurement_type: Optional[int] = None

class Measurement(MeasurementBase):
    id: int

    class Config:
        orm_mode = True
