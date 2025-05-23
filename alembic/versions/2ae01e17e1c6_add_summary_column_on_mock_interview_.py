"""add summary column on mock interview model

Revision ID: 2ae01e17e1c6
Revises: 10ffc188d48f
Create Date: 2025-03-18 16:05:11.966995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ae01e17e1c6'
down_revision: Union[str, None] = '10ffc188d48f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mock_interview', sa.Column('summary', sa.Text(), nullable=True))
    op.add_column('mock_interview', sa.Column('failed_topics', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mock_interview', 'failed_topics')
    op.drop_column('mock_interview', 'summary')
    # ### end Alembic commands ###
