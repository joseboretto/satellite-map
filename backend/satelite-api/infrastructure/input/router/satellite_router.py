from typing import List, Optional

from fastapi import APIRouter, Depends, status

from application.services.satelite_service import SatelliteService
from infrastructure.input.router.satellite_dtos import GetSatelliteResponse

SatelliteRouter = APIRouter(
    prefix="/v1/satellite", tags=["satellite"]
)


@SatelliteRouter.get("/", response_model=List[GetSatelliteResponse])
def index(
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
        satelliteService: SatelliteService = Depends(),
):
    return [
        satellite.normalize()
        for satellite in satelliteService.list(
            name, pageSize, startIndex
        )
    ]




