import datetime
import uuid


class Satellite:
    def __init__(self, id: uuid.UUID,
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

