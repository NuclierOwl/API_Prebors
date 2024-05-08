import psycopg2
from fastapi import APIRouter, Depends, HTTPException
from .connect import connect_to_db
from . import crud, schemas

router = APIRouter()


def handle_db_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except psycopg2.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    return wrapper


def handle_db_operations(func):
    def wrapper(*args, **kwargs):
        conn = connect_to_db()
        try:
            return func(*args, conn=conn, **kwargs)
        except psycopg2.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            conn.close()
    return wrapper


@router.post("/create/", response_model=schemas.SensorMeasurement)
@handle_db_operations
def create_sensor_measurement(sensor_measurement: schemas.SensorMeasurementCreate):
    return crud.create_sensor_measurement(sensor_measurement)


@router.delete("/delete/", response_model=schemas.SensorMeasurement)
@handle_db_operations
def delete_sensor_measurement(sensor_id: int, type_id: int):
    return crud.delete_sensor_measurement(sensor_id, type_id)


@router.get("/all/", response_model=schemas.SensorMeasurementList)
@handle_db_operations
def get_all_sensor_measurements():
    return {"__root__": crud.get_all_sensor_measurements()}