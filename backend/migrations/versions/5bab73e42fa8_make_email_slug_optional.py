"""make email slug optional

Revision ID: 5bab73e42fa8
Revises: 73469c266550
Create Date: 2025-03-23 12:46:30.587880

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "5bab73e42fa8"
down_revision: Union[str, None] = "73469c266550"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    with op.batch_alter_table("profiles", schema=None) as batch_op:
        batch_op.alter_column("email_slug", existing_type=sa.VARCHAR(), nullable=True)


def downgrade() -> None:
    """Downgrade schema."""

    with op.batch_alter_table("profiles", schema=None) as batch_op:
        batch_op.alter_column("email_slug", existing_type=sa.VARCHAR(), nullable=False)
