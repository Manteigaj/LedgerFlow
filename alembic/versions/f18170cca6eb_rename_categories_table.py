"""rename categories table

Revision ID: f18170cca6eb
Revises: d45149f81386
"""

from typing import Sequence, Union


revision: str = "f18170cca6eb"
down_revision: Union[str, Sequence[str], None] = "d45149f81386"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """No schema changes required."""
    pass


def downgrade() -> None:
    """No schema changes required."""
    pass
