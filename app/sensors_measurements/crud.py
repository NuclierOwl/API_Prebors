
import psycopg2
from .schemas import SensorMeasurementCreate, SensorMeasurement


def execute_sql_transaction(conn, sql, params=None, fetchone=False):
    cur = conn.cursor()
    cur.execute(sql, params)
    result = cur.fetchone() if fetchone else cur.fetchall()
    cur.close()
    conn.commit()
    return result


def create_sensor_measurement(conn, sensor_measurement: SensorMeasurementCreate):
    sql = """
    INSERT INTO sensors_measurements (sensor_id, type_id, measurement_formula)
    VALUES (%s, %s, %s)
    RETURNING sensor_id, type_id, measurement_formula;
    """
    result = execute_sql_transaction(conn, sql, (sensor_measurement.sensor_id, sensor_measurement.type_id, sensor_measurement.measurement_formula), fetchone=True)
    return SensorMeasurement(**result)


def delete_sensor_measurement(conn, sensor_id: int, type_id: int):
    sql = """
    DELETE FROM sensors_measurements
    WHERE sensor_id = %s AND type_id = %s
    RETURNING sensor_id, type_id, measurement_formula;
    """
    result = execute_sql_transaction(conn, sql, (sensor_id, type_id), fetchone=True)
    return SensorMeasurement(**result)


def get_all_sensor_measurements(conn):
    sql = """
    SELECT sensor_id, type_id, measurement_formula
    FROM sensors_measurements;
    """
    results = execute_sql_transaction(conn, sql)
    return [SensorMeasurement(**result) for result in results]