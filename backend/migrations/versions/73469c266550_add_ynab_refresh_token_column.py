"""add ynab refresh token column

Revision ID: 73469c266550
Revises: 7c1ab1c042c3
Create Date: 2025-03-23 12:30:09.849882

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "73469c266550"
down_revision: Union[str, None] = "7c1ab1c042c3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("profiles", schema=None) as batch_op:
        batch_op.add_column(sa.Column("ynab_refresh_token", sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("profiles", schema=None) as batch_op:
        batch_op.drop_column("ynab_refresh_token")
    # ### end Alembic commands ###
