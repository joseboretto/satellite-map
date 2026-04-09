from typing import List, Optional

from application.ports.input.satellite_service_port import SatelliteServicePort
from application.ports.output.satellite_repository_port import SatelliteRepositoryPort
from domain.models.satellite import Satellite


class SatelliteService(SatelliteServicePort):

    def __init__(self, repository: SatelliteRepositoryPort) -> None:
        self._repository = repository

    def list(
        self,
        name: Optional[str],
        page_size: Optional[int],
        start_index: Optional[int],
    ) -> List[Satellite]:
        print(f"SatelliteService-list. name: {name}, page_size: {page_size}, start_index: {start_index}")
        return self._repository.list(name, page_size, start_index)