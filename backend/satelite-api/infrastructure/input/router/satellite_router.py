from typing import List, Optional

from fastapi import APIRouter, Depends

from application.ports.input.satellite_service_port import SatelliteServicePort
from infrastructure.config.dependencies import get_satellite_service
from infrastructure.input.router.satellite_dtos import GetSatelliteResponse

SatelliteRouter = APIRouter(
    prefix="/api/v1/satellite", tags=["satellite"]
)


@SatelliteRouter.get("/", response_model=List[GetSatelliteResponse])
def index(
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
        satelliteService: SatelliteServicePort = Depends(get_satellite_service),
):
    satellites = satelliteService.list(name, pageSize, startIndex)
    return [
        GetSatelliteResponse(
            id=satellite.id,
            norad_id=satellite.norad_id,
            name=satellite.name,
            tle_line1=satellite.tle_line1,
            tle_line2=satellite.tle_line2,
            tle_epoch=satellite.tle_epoch,
            created_at=satellite.created_at,
            updated_at=satellite.updated_at,
        )
        for satellite in satellites
    ]
