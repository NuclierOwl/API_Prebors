from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Body, Request, Path
from .schemas import (
    MeteostationSensorCreate,
    MeteostationSensor,
    MeteostationSensorList,
    MeteostationSensorRemove,
    Meteostation,
)
from .crud import (
    create_sensor,
    update_sensor_removed_ts,
    get_all_sensors,
    get_sensor_by_inventory_number,
    get_station_by_id,
)

router = APIRouter()

@router.post("/meteostation_sensors/", response_model=MeteostationSensorList)
async def add_sensor(sensor: MeteostationSensorCreate):
    try:
        sensor_data = create_sensor(sensor)
        return MeteostationSensorList(meteostations_sensors=[sensor_data])
    except (Exception) as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put(
    "/meteostation_sensors/{sensor_inventory_number}/removed_ts",
    response_model=MeteostationSensor,
)
async def update_sensor_removed_ts_path(
    sensor_inventory_number: str = Path(..., alias="sensor_inventory_number"),
    body: MeteostationSensorRemove = Body(...),
):
    try:
        removed_ts = body.removed_ts or datetime.now()
        update_sensor_removed_ts(sensor_inventory_number, removed_ts)
        updated_sensor = get_sensor_by_inventory_number(sensor_inventory_number)
        return updated_sensor
    except (Exception) as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/meteostations_sensors/", response_model=MeteostationSensorList)
async def list_sensors(request: Request):
    try:
        sensors = get_all_sensors()
        meteostations = []
        for sensor in sensors:
            station = await get_station_by_id(sensor.station_id)
            station_dict = station.dict()
            station_dict["sensors"] = [sensor.dict()]
            meteostations.append(Meteostation(**station_dict))
        return MeteostationSensorList(meteostations_sensors=meteostations)
    except (Exception) as e:
        raise HTTPException(status_code=500, detail=str(e))