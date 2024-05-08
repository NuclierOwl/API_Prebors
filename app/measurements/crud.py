import psycopg2
from app.measurementsmain import connect_to_db

def execute_query(query, params=None, fetchone=False):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    if fetchone:
        result = cursor.fetchone()
    else:
        result = None
    conn.commit()
    cursor.close()
    conn.close()
    return result

def create_sensor_measurement(sensor_id: int, type_id: int, measurement_formula: str):
    query = """
    INSERT INTO sensors_measurements (sensor_id, type_id, measurement_formula) 
    VALUES (%s, %s, %s) RETURNING sensor_id
    """
    result = execute_query(query, (sensor_id, type_id, measurement_formula), fetchone=True)
    return {"sensor_id": result[0]}

def delete_sensor_measurement(sensor_id: int):
    query = "DELETE FROM sensors_measurements WHERE sensor_id = %s"
    execute_query(query, (sensor_id,))
    return {"message": "Sensor measurement deleted successfully"}
