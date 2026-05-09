"""Allow nullable contact additional info

Revision ID: 20260509_nullable_info
Revises: 3da2ecba51ba
Create Date: 2026-05-09 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "20260509_nullable_info"
down_revision: Union[str, None] = "3da2ecba51ba"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "contacts",
        "additional_info",
        existing_type=sa.String(length=256),
        nullable=True,
    )


def downgrade() -> None:
    op.alter_column(
        "contacts",
        "additional_info",
        existing_type=sa.String(length=256),
        nullable=False,
    )
