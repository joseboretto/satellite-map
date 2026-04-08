from pydantic import BaseModel


class GetSatelliteResponse(BaseModel):
    id: int
    norad_id: int
    name: str
    tle_line1: str
    tle_line2: str
    tle_epoch: str
    created_at: str
    updated_at: str
