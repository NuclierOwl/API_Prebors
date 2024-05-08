from app.measurements_type.connect import connect_to_db
from app.measurements_type.models import MeasurementType
from app.measurements_type.schemas import MeasurementTypeCreate, MeasurementTypeUpdate
from fastapi import HTTPException
import psycopg2


def execute_query(query, params=None, fetchone=False, fetchall=False):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()

    if fetchone:
        result = cur.fetchone()
    elif fetchall:
        result = cur.fetchall()
    else:
        result = None

    conn.close()
    return result


def create_measurement_type(measurement_type_data: MeasurementTypeCreate):
    query = "INSERT INTO public.measurements_type (type_name, type_units) VALUES (%s, %s) RETURNING type_id, type_name, type_units"
    result = execute_query(query, (measurement_type_data.type_name, measurement_type_data.type_units), fetchone=True)

    if result:
        return MeasurementType(type_id=result[0], type_name=result[1], type_units=result[2])
    return None


def get_measurement_types():
    query = "SELECT type_id, type_name, type_units FROM public.measurements_type"
    results = execute_query(query, fetchall=True)

    measurement_types = [MeasurementType(type_id=row[0], type_name=row[1], type_units=row[2]) for row in results]
    return measurement_types


def get_measurement_type(type_id: int):
    query = "SELECT type_id, type_name, type_units FROM public.measurements_type WHERE type_id = %s"
    result = execute_query(query, (type_id,), fetchone=True)

    if result:
        return MeasurementType(type_id=result[0], type_name=result[1], type_units=result[2])
    return None


def update_measurement_type(type_id: int, measurement_type_data: MeasurementTypeUpdate):
    query = "UPDATE public.measurements_type SET type_name = %s, type_units = %s WHERE type_id = %s RETURNING type_id, type_name, type_units"
    result = execute_query(query, (measurement_type_data.type_name, measurement_type_data.type_units, type_id),
                           fetchone=True)

    if result:
        return MeasurementType(type_id=result[0], type_name=result[1], type_units=result[2])
    return None


def delete_measurement_type(type_id: int):
    query = "DELETE FROM public.measurements_type WHERE type_id = %s RETURNING type_id, type_name, type_units"
    result = execute_query(query, (type_id,), fetchone=True)

    if result:
        return MeasurementType(type_id=result[0], type_name=result[1], type_units=result[2])
    return None
