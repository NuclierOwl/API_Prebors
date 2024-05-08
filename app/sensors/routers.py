from fastapi import APIRouter, HTTPException
from typing import List
from app.sensors.schemas import Sensor, SensorCreate, SensorUpdate
from app.sensors import crud

router = APIRouter()

@router.get("/sensors/", response_model=List[Sensor])
async def read_sensors():
    return crud.get_sensors()

@router.post("/sensors/", response_model=Sensor)
async def create_sensor(sensor: SensorCreate):
    return crud.create_sensor(sensor)

@router.put("/sensors/{sensor_id}", response_model=Sensor)
async def update_sensor(sensor_id: int, sensor: SensorUpdate):
    db_sensor = crud.get_sensor(sensor_id)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return crud.update_sensor(sensor_id, sensor)

@router.get("/sensors/{sensor_id}", response_model=Sensor)
async def read_sensor(sensor_id: int):
    db_sensor = crud.get_sensor(sensor_id)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return db_sensor

@router.delete("/sensors/{sensor_id}", response_model=Sensor)
async def delete_sensor(sensor_id: int):
    db_sensor = crud.get_sensor(sensor_id)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    crud.delete_sensor(sensor_id)
    return db_sensor