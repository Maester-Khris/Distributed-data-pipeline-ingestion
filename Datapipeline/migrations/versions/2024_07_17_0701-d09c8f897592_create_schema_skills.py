"""create schema skills

Revision ID: d09c8f897592
Revises: 
Create Date: 2024-07-17 07:01:46.650940

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd09c8f897592'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE SCHEMA IF NOT EXISTS projects;')

def downgrade() -> None:
    p.execute('DROP SCHEMA IF EXISTS projects CASCADE;')
