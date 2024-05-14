from fastapi import FastAPI
from app.sensors import routers as sensors_routers
from app.measurements_type import routers as measurements_type_routers
from app.sensors_measurements import routers as sensors_measurements_routers
from app.measurements import routers as measurements_routers
from app.meteostatins import routers as meteostations_routers
from app.meteostation_sensor import routers as meteostation_sensors_routers

app = FastAPI()

app.include_router(sensors_routers.router, prefix="/sensors", tags=["sensors"])
app.include_router(measurements_type_routers.router, prefix="/measurement_types", tags=["measurement_types"])
app.include_router(sensors_measurements_routers.router, prefix="/sensors_measurements", tags=["sensors_measurements"])
app.include_router(measurements_routers.router, prefix="/measurements", tags=["measurements"])
app.include_router(meteostations_routers.router, prefix="/meteostations", tags=["meteostations"])
app.include_router(meteostation_sensors_routers.router, prefix="/meteostation_sensors", tags=["meteostation_sensors"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="193.176.78.35", port=5433)
