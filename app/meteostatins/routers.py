from fastapi import APIRouter, HTTPException
from typing import List
from app.meteostatins import crud, schemas

router = APIRouter()


@router.post("/", response_model=schemas.Meteostation)
def create_meteostation(meteostation: schemas.MeteostationCreate):
    return crud.create_meteostation(meteostation)


@router.get("/", response_model=List[schemas.Meteostation])
def get_all_meteostations():
    return crud.get_all_meteostations()


@router.get("/{station_id}", response_model=schemas.Meteostation)
def get_meteostation(station_id: int):
    db_meteostation = crud.get_meteostation_by_id(station_id)
    if db_meteostation is None:
        raise HTTPException(status_code=404, detail="Meteostation not found")
    return db_meteostation


@router.put("/{station_id}", response_model=schemas.Meteostation)
def update_meteostation(station_id: int, meteostation: schemas.MeteostationUpdate):
    db_meteostation = crud.update_meteostation(station_id, meteostation)
    if db_meteostation is None:
        raise HTTPException(status_code=404, detail="Meteostation not found")
    return db_meteostation


@router.delete("/{station_id}", response_model=schemas.Meteostation)
def delete_meteostation(station_id: int):
    db_meteostation = crud.delete_meteostation(station_id)
    if db_meteostation is None:
        raise HTTPException(status_code=404, detail="Meteostation not found")
    return db_meteostation