from pydantic import BaseModel


class MeteostationSensor(BaseModel):
    sensor_inventory_number: str
    station_id: int
    sensor_id: int
    added_ts: str
    removed_ts: str
