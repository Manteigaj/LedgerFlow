"""add users and user relationship

Revision ID: 218c954ee24d
Revises: f18170cca6eb
Create Date: 2026-08-15 22:49:09.414485
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "218c954ee24d"
down_revision: Union[str, Sequence[str], None] = "f18170cca6eb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )

    op.create_unique_constraint(
        "uq_categories_name",
        "categories",
        ["name"],
    )

    op.add_column(
        "transactions",
        sa.Column("user_id", sa.Integer(), nullable=True),
    )

    op.create_foreign_key(
        "fk_transactions_user_id",
        "transactions",
        "users",
        ["user_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        "fk_transactions_user_id",
        "transactions",
        type_="foreignkey",
    )

    op.drop_column(
        "transactions",
        "user_id",
    )

    op.drop_constraint(
        "uq_categories_name",
        "categories",
        type_="unique",
    )

    op.drop_table("users")
