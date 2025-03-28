"""create users table

Revision ID: 6669f81cd356
Revises: 52deef494495
Create Date: 2025-03-28 07:34:36.194788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6669f81cd356'
down_revision: Union[str, None] = '52deef494495'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
