"""add uuid to problems

Revision ID: 20260720_0002
Revises: 30536251e849
Create Date: 2026-07-20
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


revision: str = "20260720_0002"
down_revision: Union[str, Sequence[str], None] = "30536251e849"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "problems",
        sa.Column(
            "uuid",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
    )
    op.create_index(op.f("ix_problems_uuid"), "problems", ["uuid"], unique=True)


def downgrade() -> None:
    op.drop_index(op.f("ix_problems_uuid"), table_name="problems")
    op.drop_column("problems", "uuid")
