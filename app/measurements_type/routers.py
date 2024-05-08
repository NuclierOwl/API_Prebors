from fastapi import APIRouter, HTTPException
from typing import List

from app.measurements_type.schemas import MeasurementType, MeasurementTypeCreate, MeasurementTypeUpdate
from app.measurements_type import crud

router = APIRouter()

@router.post("/measurement_types/", response_model=MeasurementType)
async def create_measurement_type(measurement_type_data: MeasurementTypeCreate):
    return crud.create_measurement_type(measurement_type_data)

@router.get("/measurement_types/", response_model=List[MeasurementType])
async def read_measurement_types():
    return crud.get_measurement_types()

@router.get("/measurement_types/{type_id}", response_model=MeasurementType)
async def read_measurement_type(type_id: int):
    measurement_type = crud.get_measurement_type(type_id)
    if not measurement_type:
        raise HTTPException(status_code=404, detail="Measurement type not found")
    return measurement_type

@router.put("/measurement_types/{type_id}", response_model=MeasurementType)
async def update_measurement_type(type_id: int, measurement_type_data: MeasurementTypeUpdate):
    updated_measurement_type = crud.update_measurement_type(type_id, measurement_type_data)
    if not updated_measurement_type:
        raise HTTPException(status_code=404, detail="Measurement type not found")
    return updated_measurement_type

@router.delete("/measurement_types/{type_id}", response_model=MeasurementType)
async def delete_measurement_type(type_id: int):
    deleted_measurement_type = crud.delete_measurement_type(type_id)
    if not deleted_measurement_type:
        raise HTTPException(status_code=404, detail="Measurement type not found")
    return deleted_measurement_type
