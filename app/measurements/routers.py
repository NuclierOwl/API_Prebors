from fastapi import APIRouter, Depends, HTTPException
import psycopg2

from app.sensors_measurements import crud

router = APIRouter()


@router.post("/", response_model=dict)
def create_sensor_measurement(sensor_id: int, type_id: int, measurement_formula: str):
    try:
        return crud.create_sensor_measurement(sensor_id, type_id, measurement_formula)
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{sensor_id}", response_model=dict)
def delete_sensor_measurement(sensor_id: int):
    try:
        return crud.delete_sensor_measurement(sensor_id)
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=str(e))