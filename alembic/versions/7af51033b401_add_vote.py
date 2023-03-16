"""add-vote

Revision ID: 7af51033b401
Revises: a0ab82a21c95
Create Date: 2023-03-16 21:32:35.364558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7af51033b401'
down_revision = 'a0ab82a21c95'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("votes",
                    sa.Column("user_id", sa.Integer(), nullable=False),
                    sa.Column("post_id", sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(["post_id"], ["posts.id"],  ondelete="CASCADE"),
                    sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint("user_id", "post_id"))


def downgrade() -> None:
    op.drop_table("votes")
