from typing import Optional, List

from fastapi import Depends

from infrastructure.output.database.repositories.satelite_repository import SatelliteRepository
from infrastructure.output.database.schema.satellite_schema import SatelliteSchema


class SatelliteService:
    satelliteRepository: SatelliteRepository

    def __init__(
            self, satelliteRepository: SatelliteRepository = Depends()
    ) -> None:
        self.satelliteRepository = satelliteRepository

    def list(self,
             name: Optional[str],
             pageSize: Optional[int],
             startIndex: Optional[int]) -> List[SatelliteSchema]:
        return self.satelliteRepository.list(
            name, pageSize, startIndex
        )
