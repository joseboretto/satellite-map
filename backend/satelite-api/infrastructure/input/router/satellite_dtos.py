import datetime
import uuid

from pydantic import BaseModel


class GetSatelliteResponse(BaseModel):
    id: uuid.UUID
    norad_id: int
    name: str
    tle_line1: str
    tle_line2: str
    tle_epoch: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
