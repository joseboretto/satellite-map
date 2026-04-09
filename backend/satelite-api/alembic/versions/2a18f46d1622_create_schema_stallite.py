"""create schema stallite

Revision ID: 2a18f46d1622
Revises: 
Create Date: 2026-04-08 15:02:15.976920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a18f46d1622'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # todo: alembic use as default schema "satellite", so we need to create it manually.
    op.execute('CREATE SCHEMA IF NOT EXISTS satellite;')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute('DROP SCHEMA IF EXISTS satellite CASCADE;')
    pass
