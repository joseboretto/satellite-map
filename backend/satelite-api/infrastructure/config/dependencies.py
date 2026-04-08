from fastapi import Depends
from sqlalchemy.orm import Session

from application.ports.input.satellite_service_port import SatelliteServicePort
from application.services.satelite_service import SatelliteService
from infrastructure.output.database.config.database_config import get_db_connection
from infrastructure.output.database.repositories.satelite_repository import SatelliteRepository


def get_satellite_service(db: Session = Depends(get_db_connection)) -> SatelliteServicePort:
    return SatelliteService(repository=SatelliteRepository(db=db))
