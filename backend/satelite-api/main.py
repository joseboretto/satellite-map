import os
import sys

# Make sure we can import our application taking into account the current working directory.
# This is needed for the application to be able to import modules from the parent directory.
# This is needed by Vercel monorepo deployment.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI

from infrastructure.config.env import get_environment_variables
from infrastructure.input.router.healthcheck_router import HealthCheckRouter
from infrastructure.input.router.satellite_router import SatelliteRouter

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    redirect_slashes=False
)

# Add Routers
app.include_router(SatelliteRouter)
app.include_router(HealthCheckRouter)
