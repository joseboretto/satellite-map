from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from infrastructure.output.database.config.database_config import (
    get_db_connection,
)
from infrastructure.output.database.schema.satellite_schema import SatelliteSchema


class SatelliteRepository:
    db: Session

    def __init__(
            self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(
            self,
            name: Optional[str],
            limit: Optional[int],
            start: Optional[int],
    ) -> List[SatelliteSchema]:
        query = self.db.query(SatelliteSchema)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()
