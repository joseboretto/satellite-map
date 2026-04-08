from abc import ABC, abstractmethod
from typing import List, Optional

from domain.models.satellite import Satellite


class SatelliteRepositoryPort(ABC):

    @abstractmethod
    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Satellite]:
        ...