from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class MeteostationSensorBase(BaseModel):
    station_id: int
    sensor_id: int


class MeteostationSensorCreate(MeteostationSensorBase):
    added_ts: Optional[datetime] = Field(default_factory=datetime.now, alias="added_ts")
    removed_ts: Optional[datetime] = Field(None, alias="removed_ts")


class MeteostationSensor(MeteostationSensorBase):
    sensor_inventory_number: str = Field(..., alias="sensor_inventory_number")
    added_ts: datetime = Field(..., alias="added_ts")
    removed_ts: Optional[datetime] = Field(None, alias="removed_ts")


class MeteostationSensorRemove(BaseModel):
    removed_ts: datetime = Field(..., alias="removed_ts")


class MeteostationSensorList(BaseModel):
    meteostations_sensors: List[MeteostationSensor]


class Meteostation(BaseModel):
    station_id: int
    station_name: str
    station_longitude: float
    station_latitude: float
    sensors: List[MeteostationSensor]
