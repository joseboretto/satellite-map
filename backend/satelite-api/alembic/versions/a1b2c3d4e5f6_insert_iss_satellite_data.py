"""insert ISS satellite data

Revision ID: a1b2c3d4e5f6
Revises: 13840232f503
Create Date: 2026-04-08 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = '13840232f503'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# ISS (ZARYA) — NORAD ID 25544
# TLE valid as of 2026-04-07 (epoch derived from TLE line 1 field 4: 26097.55490884)
ISS_ID = 'e1a2b3c4-d5e6-7f8a-9b0c-d1e2f3a4b5c6'
ISS_NORAD_ID = 25544
ISS_NAME = 'ISS (ZARYA)'
ISS_TLE_LINE1 = '1 25544U 98067A   26097.55490884  .00020147  00000+0  35935-3 0  9999'
ISS_TLE_LINE2 = '2 25544  51.6403 330.4833 0003778 248.4090 111.6649 15.50171704502616'
# Epoch: day 97.55490884 of 2026 → 2026-04-07 13:19:04 UTC
ISS_TLE_EPOCH = '2026-04-07 13:19:04+00'


def upgrade() -> None:
    """Insert ISS satellite seed data."""
    op.execute(
        f"""
        INSERT INTO satellite.satellites
            (id, norad_id, name, tle_line1, tle_line2, tle_epoch, created_at, updated_at)
        VALUES
            (
                '{ISS_ID}',
                {ISS_NORAD_ID},
                '{ISS_NAME}',
                '{ISS_TLE_LINE1}',
                '{ISS_TLE_LINE2}',
                '{ISS_TLE_EPOCH}',
                NOW(),
                NOW()
            )
        ON CONFLICT (id) DO NOTHING;
        """
    )


def downgrade() -> None:
    """Remove ISS satellite seed data."""
    op.execute(
        f"DELETE FROM satellite.satellites WHERE norad_id = {ISS_NORAD_ID};"
    )