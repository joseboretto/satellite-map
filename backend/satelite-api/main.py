from fastapi import FastAPI

from infrastructure.config.env import get_environment_variables
from infrastructure.input.router.healthcheck_router import HealthCheckRouter
from infrastructure.input.router.satellite_router import SatelliteRouter

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI()

# Add Routers
app.include_router(SatelliteRouter)
app.include_router(HealthCheckRouter)
