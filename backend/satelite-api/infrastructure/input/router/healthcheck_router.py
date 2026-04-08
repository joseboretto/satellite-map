from fastapi import APIRouter

HealthCheckRouter = APIRouter(
    prefix="/api/v1/healthcheck", tags=["healthcheck"]
)


@HealthCheckRouter.get("")
def index():
    return {
        "status": "ok",
    }
