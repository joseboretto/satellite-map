from fastapi import APIRouter

HealthCheckRouter = APIRouter(
    prefix="/v1/healthcheck", tags=["healthcheck"]
)


@HealthCheckRouter.get("/")
def index():
    return {
        "status": "ok",
    }
