from typing import List, Optional
from app.meteostatins.models import Meteostation, MeteostationCreate, MeteostationUpdate
from app.meteostatins.schemas import Meteostation as MeteostationSchema
from app.meteostatins.connect import connect_to_db

def execute_query(query: str, params: Optional[tuple] = None, fetch_one: bool = False) -> Optional[List]:
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute(query, params) if params else cur.execute(query)
    result = cur.fetchone() if fetch_one else cur.fetchall()
    conn.commit()
    conn.close()
    return result

def create_meteostation(meteostation: MeteostationCreate) -> Meteostation:
    query = "INSERT INTO public.meteostatins (station_name, station_longitude, station_latitude) VALUES (%s, %s, %s) RETURNING station_id, station_name, station_longitude, station_latitude"
    result = execute_query(query, (meteostation.station_name, meteostation.station_longitude, meteostation.station_latitude), fetch_one=True)
    return Meteostation(station_id=result[0], station_name=result[1], station_longitude=result[2], station_latitude=result[3])

def get_all_meteostations() -> List[Meteostation]:
    query = "SELECT station_id, station_name, station_longitude, station_latitude FROM public.meteostatins"
    results = execute_query(query)
    return [Meteostation(station_id=row[0], station_name=row[1], station_longitude=row[2], station_latitude=row[3]) for row in results]

def get_meteostation_by_id(station_id: int) -> Optional[Meteostation]:
    query = "SELECT station_id, station_name, station_longitude, station_latitude FROM public.meteostatins WHERE station_id = %s"
    result = execute_query(query, (station_id,), fetch_one=True)
    return Meteostation(station_id=result[0], station_name=result[1], station_longitude=result[2], station_latitude=result[3]) if result else None

def update_meteostation(station_id: int, meteostation: MeteostationUpdate) -> Optional[Meteostation]:
    query = "UPDATE public.meteostatins SET station_name = %s, station_longitude = %s, station_latitude = %s WHERE station_id = %s RETURNING station_id, station_name, station_longitude, station_latitude"
    result = execute_query(query, (meteostation.station_name, meteostation.station_longitude, meteostation.station_latitude, station_id), fetch_one=True)
    return Meteostation(station_id=result[0], station_name=result[1], station_longitude=result[2], station_latitude=result[3]) if result else None

def delete_meteostation(station_id: int) -> Optional[Meteostation]:
    query = "DELETE FROM public.meteostatins WHERE station_id = %s RETURNING station_id, station_name, station_longitude, station_latitude"
    result = execute_query(query, (station_id,), fetch_one=True)
    return Meteostation(station_id=result[0], station_name=result[1], station_longitude=result[2], station_latitude=result[3]) if result else None
