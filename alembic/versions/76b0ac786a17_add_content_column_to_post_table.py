"""add content column to post table

Revision ID: 76b0ac786a17
Revises: 7e2675cb402f
Create Date: 2023-03-15 23:14:38.477582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76b0ac786a17'
down_revision = '7e2675cb402f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
