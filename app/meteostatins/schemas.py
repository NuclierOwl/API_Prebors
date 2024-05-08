from typing import List, Optional
from pydantic import BaseModel


class MeteostationBase(BaseModel):
    station_name: str
    station_longitude: float
    station_latitude: float


class MeteostationCreate(MeteostationBase):
    pass


class MeteostationUpdate(MeteostationBase):
    pass


class Meteostation(MeteostationBase):
    station_id: int

    class Config:
        orm_mode = True
