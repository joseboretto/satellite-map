from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from application.ports.output.satellite_repository_port import SatelliteRepositoryPort
from domain.models.satellite import Satellite
from infrastructure.output.database.config.database_config import get_db_connection
from infrastructure.output.database.schema.satellite_schema import SatelliteSchema


class SatelliteRepository(SatelliteRepositoryPort):

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Satellite]:
        query = self.db.query(SatelliteSchema)

        if name:
            query = query.filter_by(name=name)

        rows = query.offset(start).limit(limit).all()
        return [self._to_domain(row) for row in rows]

    def _to_domain(self, row: SatelliteSchema) -> Satellite:
        return Satellite(
            id=row.id,
            norad_id=row.norad_id,
            name=row.name,
            tle_line1=row.tle_line1,
            tle_line2=row.tle_line2,
            tle_epoch=row.tle_epoch,
            created_at=row.created_at,
            updated_at=row.updated_at,
        )
