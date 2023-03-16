"""Create posts table

Revision ID: 7e2675cb402f
Revises: 
Create Date: 2023-03-15 23:04:03.028477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e2675cb402f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String, nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
