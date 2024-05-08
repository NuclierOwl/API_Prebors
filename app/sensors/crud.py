from app.sensors.models import Sensor
from app.sensors.connect import connect_to_db

def execute_query(query, params=None, fetch_one=False):
    with connect_to_db() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            result = cur.fetchone() if fetch_one else cur.fetchall()
            conn.commit()
    return result

def get_sensors():
    query = "SELECT sensor_id, sensor_name FROM public.sensors"
    rows = execute_query(query, fetch_one=False)
    sensors = [Sensor(sensor_id=row[0], sensor_name=row[1]) for row in rows]
    return sensors

def create_sensor(sensor_data):
    query = "INSERT INTO public.sensors (sensor_id, sensor_name) VALUES (%s, %s) RETURNING sensor_id, sensor_name"
    created_sensor = execute_query(query, (sensor_data.sensor_id, sensor_data.sensor_name), fetch_one=True)
    return Sensor(sensor_id=created_sensor[0], sensor_name=created_sensor[1])

def get_sensor(sensor_id: int):
    query = "SELECT sensor_id, sensor_name FROM public.sensors WHERE sensor_id = %s"
    sensor = execute_query(query, (sensor_id,), fetch_one=True)
    return Sensor(sensor_id=sensor[0], sensor_name=sensor[1]) if sensor else None

def update_sensor(sensor_id: int, sensor_data):
    query = "UPDATE public.sensors SET sensor_name = %s WHERE sensor_id = %s RETURNING sensor_id, sensor_name"
    updated_sensor = execute_query(query, (sensor_data.sensor_name, sensor_id), fetch_one=True)
    return Sensor(sensor_id=updated_sensor[0], sensor_name=updated_sensor[1]) if updated_sensor else None

def delete_sensor(sensor_id: int):
    query = "DELETE FROM public.sensors WHERE sensor_id = %s RETURNING sensor_id, sensor_name"
    deleted_sensor = execute_query(query, (sensor_id,), fetch_one=True)
    return Sensor(sensor_id=deleted_sensor[0], sensor_name=deleted_sensor[1]) if deleted_sensor else None