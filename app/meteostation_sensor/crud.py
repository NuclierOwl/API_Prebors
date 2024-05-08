from typing import List
from datetime import datetime
from psycopg2 import connect, Error
from psycopg2.extras import RealDictCursor
from .schemas import MeteostationSensorCreate, MeteostationSensor, Meteostation
from .connect import connect_to_db


def create_sensor(sensor: MeteostationSensorCreate) -> MeteostationSensor:
    conn = connect_to_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    added_ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Check if the sensor already exists
        cur.execute(
            """
            SELECT * FROM meteostation_sensor
            WHERE sensor_inventory_number = %s
            """,
            (sensor.sensor_inventory_number,),
        )
        if cur.fetchone():
            raise ValueError("Sensor inventory number already exists")

        cur.execute(
            """
            INSERT INTO meteostation_sensor (sensor_inventory_number, station_id, sensor_id, added_ts, removed_ts)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING *
            """,
            (sensor.sensor_inventory_number, sensor.station_id, sensor.sensor_id, added_ts, sensor.removed_ts)
        )
        sensor_data = cur.fetchone()
        cur.close()
        conn.close()
        return MeteostationSensor(**sensor_data)
    except (Error, ValueError) as e:
        cur.close()
        conn.close()
        raise e


def update_sensor_removed_ts(sensor_inventory_number: str, removed_ts: datetime):
    conn = connect_to_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    removed_ts = removed_ts.strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(
        """
        UPDATE meteostation_sensor
        SET removed_ts = %s
        WHERE sensor_inventory_number = %s
        """,
        (removed_ts, sensor_inventory_number)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_all_sensors() -> List[MeteostationSensor]:
    conn = connect_to_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT station_id, sensor_id, sensor_inventory_number, added_ts, removed_ts
        FROM meteostation_sensor
    """)
    sensors = cur.fetchall()
    cur.close()
    conn.close()

    return [MeteostationSensor(**sensor) for sensor in sensors]


def get_sensor_by_inventory_number(sensor_inventory_number: str) -> MeteostationSensor:
    conn = connect_to_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT station_id, sensor_id, sensor_inventory_number, added_ts, removed_ts
        FROM meteostation_sensor
        WHERE sensor_inventory_number = %s
    """, (sensor_inventory_number,))
    sensor_data = cur.fetchone()
    cur.close()
    conn.close()

    if not sensor_data:
        raise ValueError(f"Sensor inventory number {sensor_inventory_number} does not exist")

    return MeteostationSensor(**sensor_data)


def get_station_by_id(station_id: int) -> Meteostation:
    conn = connect_to_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT *
        FROM meteostations
        WHERE station_id = %s
    """, (station_id,))
    station_data = cur.fetchone()
    cur.close()
    conn.close()

    if not station_data:
        raise ValueError(f"Station with ID {station_id} does not exist")

    return Meteostation(**station_data)


def create_meteostation(sensor: MeteostationSensorCreate) -> MeteostationSensor:
    conn = connect_to_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    added_ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Check if the meteostation exists
        cur.execute(
            """
            SELECT * FROM meteostations
            WHERE station_id = %s
            """,
            (sensor.station_id,),
        )
        if not cur.fetchone():
            raise ValueError("Meteostation with given station_id does not exist")

        cur.execute(
            """
            INSERT INTO meteostation_sensor (sensor_inventory_number, station_id, sensor_id, added_ts, removed_ts)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING *
            """,
            (sensor.sensor_inventory_number, sensor.station_id, sensor.sensor_id, added_ts, sensor.removed_ts)
        )
        sensor_data = cur.fetchone()
        cur.close()
        conn.close()
        return MeteostationSensor(**sensor_data)
    except (Error, ValueError) as e:
        cur.close()
        conn.close()
        raise e