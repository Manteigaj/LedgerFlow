"""internationalize transaction tables

Revision ID: d45149f81386
Revises: d4ac952bb293
Create Date: 2026-08-14 21:20:18.620148

"""

from typing import Sequence, Union

from alembic import op


revision: str = "d45149f81386"
down_revision: Union[str, Sequence[str], None] = "d4ac952bb293"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Rename transaction table and columns to English."""

    op.rename_table("transacoes", "transactions")

    op.alter_column(
        "transactions",
        "data",
        new_column_name="date",
    )

    op.alter_column(
        "transactions",
        "descricao",
        new_column_name="description",
    )

    op.alter_column(
        "transactions",
        "valor",
        new_column_name="amount",
    )

    op.alter_column(
        "transactions",
        "categoria_id",
        new_column_name="category_id",
    )


def downgrade() -> None:
    """Restore Portuguese transaction table and columns."""

    op.alter_column(
        "transactions",
        "category_id",
        new_column_name="categoria_id",
    )

    op.alter_column(
        "transactions",
        "amount",
        new_column_name="valor",
    )

    op.alter_column(
        "transactions",
        "description",
        new_column_name="descricao",
    )

    op.alter_column(
        "transactions",
        "date",
        new_column_name="data",
    )

    op.rename_table("transactions", "transacoes")
