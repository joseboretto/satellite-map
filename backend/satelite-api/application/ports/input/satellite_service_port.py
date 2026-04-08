from abc import ABC, abstractmethod
from typing import List, Optional

from domain.models.satellite import Satellite


class SatelliteServicePort(ABC):

    @abstractmethod
    def list(
        self,
        name: Optional[str],
        page_size: Optional[int],
        start_index: Optional[int],
    ) -> List[Satellite]:
        ...