"""add last few columns to post table

Revision ID: ad1fb7076e44
Revises: d7b8f2afa7ef
Create Date: 2023-03-16 20:26:06.858679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad1fb7076e44'
down_revision = 'd7b8f2afa7ef'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                     nullable=False, server_default=sa.text("NOW()")),)


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
