import datetime
import uuid

from sqlalchemy import Column, Integer, String, UUID, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base class
Base = declarative_base()


class SatelliteSchema(Base):
    __tablename__ = 'satellites'
    id = Column(UUID, primary_key=True)
    norad_id = Column(Integer)
    name = Column(String)
    tle_line1 = Column(String)
    tle_line2 = Column(String)
    tle_epoch = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self,
                 id: uuid.UUID,
                 norad_id: int,
                 name: str,
                 tle_line1: str,
                 tle_line2: str,
                 tle_epoch: datetime.datetime,
                 created_at: datetime.datetime,
                 updated_at: datetime.datetime):
        self.id = id
        self.norad_id = norad_id
        self.name = name
        self.tle_line1 = tle_line1
        self.tle_line2 = tle_line2
        self.tle_epoch = tle_epoch
        self.created_at = created_at
        self.updated_at = updated_at
