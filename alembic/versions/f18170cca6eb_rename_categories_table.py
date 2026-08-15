"""rename categories table

Revision ID: f18170cca6eb
Revises: d45149f81386
"""

from typing import Sequence, Union

from alembic import op


revision: str = "f18170cca6eb"
down_revision: Union[str, Sequence[str], None] = "d45149f81386"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Rename categories table and column."""

    op.rename_table("categorias", "categories")

    op.alter_column(
        "categories",
        "nome",
        new_column_name="name",
    )


def downgrade() -> None:
    """Restore categories table and column."""

    op.alter_column(
        "categories",
        "name",
        new_column_name="nome",
    )

    op.rename_table("categories", "categorias")
