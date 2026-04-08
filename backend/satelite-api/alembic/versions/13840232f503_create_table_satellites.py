"""create table satellites

Revision ID: 13840232f503
Revises: 2a18f46d1622
Create Date: 2026-04-08 15:08:28.483258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13840232f503'
down_revision: Union[str, Sequence[str], None] = '2a18f46d1622'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS satellite.satellites
        (
            id         uuid PRIMARY KEY,
            norad_id   int          NOT NULL,
            name       varchar(255) NOT NULL,
            tle_line1  varchar(69)  NOT NULL,
            tle_line2  varchar(69)  NOT NULL,
            tle_epoch  timestamptz  NOT NULL,
            created_at timestamptz  NOT NULL,
            updated_at timestamptz  NOT NULL
            );
        """)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP TABLE IF EXISTS satellite.satellites;")
    pass
