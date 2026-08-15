"""internationalize category table

Revision ID: d4ac952bb293
Revises: 0fd14954723d
Create Date: 2026-08-10 14:13:25.383231

"""

from typing import Sequence, Union

from alembic import op


revision: str = "d4ac952bb293"
down_revision: Union[str, Sequence[str], None] = "0fd14954723d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Rename category table and column to English."""

    op.rename_table("categorias", "categories")

    op.alter_column(
        "categories",
        "nome",
        new_column_name="name",
    )


def downgrade() -> None:
    """Restore Portuguese category table and column."""

    op.alter_column(
        "categories",
        "name",
        new_column_name="nome",
    )

    op.rename_table("categories", "categorias")
