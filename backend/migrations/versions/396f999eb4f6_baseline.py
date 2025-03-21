"""Baseline

Revision ID: 396f999eb4f6
Revises: 
Create Date: 2025-03-17 10:35:13.877868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '396f999eb4f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('is_sso_user', sa.Boolean(), server_default=sa.text('false'), nullable=False, comment='Auth: Set this column to true when the account comes from SSO. These accounts can have duplicate emails.'),
    sa.Column('is_anonymous', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('instance_id', sa.Uuid(), nullable=True),
    sa.Column('aud', sa.String(length=255), nullable=True),
    sa.Column('role', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('encrypted_password', sa.String(length=255), nullable=True),
    sa.Column('email_confirmed_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('invited_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('confirmation_token', sa.String(length=255), nullable=True),
    sa.Column('confirmation_sent_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('recovery_token', sa.String(length=255), nullable=True),
    sa.Column('recovery_sent_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('email_change_token_new', sa.String(length=255), nullable=True),
    sa.Column('email_change', sa.String(length=255), nullable=True),
    sa.Column('email_change_sent_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('last_sign_in_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('raw_app_meta_data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('raw_user_meta_data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('is_super_admin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('phone', sa.Text(), server_default=sa.text('NULL::character varying'), nullable=True),
    sa.Column('phone_confirmed_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('phone_change', sa.Text(), server_default=sa.text("''::character varying"), nullable=True),
    sa.Column('phone_change_token', sa.String(length=255), server_default=sa.text("''::character varying"), nullable=True),
    sa.Column('phone_change_sent_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('confirmed_at', sa.DateTime(timezone=True), sa.Computed('LEAST(email_confirmed_at, phone_confirmed_at)', persisted=True), nullable=True),
    sa.Column('email_change_token_current', sa.String(length=255), server_default=sa.text("''::character varying"), nullable=True),
    sa.Column('email_change_confirm_status', sa.SmallInteger(), server_default=sa.text('0'), nullable=True),
    sa.Column('banned_until', sa.DateTime(timezone=True), nullable=True),
    sa.Column('reauthentication_token', sa.String(length=255), server_default=sa.text("''::character varying"), nullable=True),
    sa.Column('reauthentication_sent_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.CheckConstraint('email_change_confirm_status >= 0 AND email_change_confirm_status <= 2', name='users_email_change_confirm_status_check'),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('phone', name='users_phone_key'),
    schema='auth',
    comment='Auth: Stores user login data within a secure schema.'
    )
    with op.batch_alter_table('users', schema='auth') as batch_op:
        batch_op.create_index('confirmation_token_idx', ['confirmation_token'], unique=True)
        batch_op.create_index('email_change_token_current_idx', ['email_change_token_current'], unique=True)
        batch_op.create_index('email_change_token_new_idx', ['email_change_token_new'], unique=True)
        batch_op.create_index('reauthentication_token_idx', ['reauthentication_token'], unique=True)
        batch_op.create_index('recovery_token_idx', ['recovery_token'], unique=True)
        batch_op.create_index('users_email_partial_key', ['email'], unique=True)
        batch_op.create_index('users_instance_id_email_idx', ['instance_id'], unique=False)
        batch_op.create_index('users_instance_id_idx', ['instance_id'], unique=False)
        batch_op.create_index('users_is_anonymous_idx', ['is_anonymous'], unique=False)

    op.create_table('pg_stat_statements',
    sa.Column('userid', postgresql.OID(), nullable=True),
    sa.Column('dbid', postgresql.OID(), nullable=True),
    sa.Column('toplevel', sa.Boolean(), nullable=True),
    sa.Column('queryid', sa.BigInteger(), nullable=True),
    sa.Column('query', sa.Text(), nullable=True),
    sa.Column('plans', sa.BigInteger(), nullable=True),
    sa.Column('total_plan_time', sa.Double(precision=53), nullable=True),
    sa.Column('min_plan_time', sa.Double(precision=53), nullable=True),
    sa.Column('max_plan_time', sa.Double(precision=53), nullable=True),
    sa.Column('mean_plan_time', sa.Double(precision=53), nullable=True),
    sa.Column('stddev_plan_time', sa.Double(precision=53), nullable=True),
    sa.Column('calls', sa.BigInteger(), nullable=True),
    sa.Column('total_exec_time', sa.Double(precision=53), nullable=True),
    sa.Column('min_exec_time', sa.Double(precision=53), nullable=True),
    sa.Column('max_exec_time', sa.Double(precision=53), nullable=True),
    sa.Column('mean_exec_time', sa.Double(precision=53), nullable=True),
    sa.Column('stddev_exec_time', sa.Double(precision=53), nullable=True),
    sa.Column('rows', sa.BigInteger(), nullable=True),
    sa.Column('shared_blks_hit', sa.BigInteger(), nullable=True),
    sa.Column('shared_blks_read', sa.BigInteger(), nullable=True),
    sa.Column('shared_blks_dirtied', sa.BigInteger(), nullable=True),
    sa.Column('shared_blks_written', sa.BigInteger(), nullable=True),
    sa.Column('local_blks_hit', sa.BigInteger(), nullable=True),
    sa.Column('local_blks_read', sa.BigInteger(), nullable=True),
    sa.Column('local_blks_dirtied', sa.BigInteger(), nullable=True),
    sa.Column('local_blks_written', sa.BigInteger(), nullable=True),
    sa.Column('temp_blks_read', sa.BigInteger(), nullable=True),
    sa.Column('temp_blks_written', sa.BigInteger(), nullable=True),
    sa.Column('blk_read_time', sa.Double(precision=53), nullable=True),
    sa.Column('blk_write_time', sa.Double(precision=53), nullable=True),
    sa.Column('temp_blk_read_time', sa.Double(precision=53), nullable=True),
    sa.Column('temp_blk_write_time', sa.Double(precision=53), nullable=True),
    sa.Column('wal_records', sa.BigInteger(), nullable=True),
    sa.Column('wal_fpi', sa.BigInteger(), nullable=True),
    sa.Column('wal_bytes', sa.Numeric(), nullable=True),
    sa.Column('jit_functions', sa.BigInteger(), nullable=True),
    sa.Column('jit_generation_time', sa.Double(precision=53), nullable=True),
    sa.Column('jit_inlining_count', sa.BigInteger(), nullable=True),
    sa.Column('jit_inlining_time', sa.Double(precision=53), nullable=True),
    sa.Column('jit_optimization_count', sa.BigInteger(), nullable=True),
    sa.Column('jit_optimization_time', sa.Double(precision=53), nullable=True),
    sa.Column('jit_emission_count', sa.BigInteger(), nullable=True),
    sa.Column('jit_emission_time', sa.Double(precision=53), nullable=True)
    )
    op.create_table('pg_stat_statements_info',
    sa.Column('dealloc', sa.BigInteger(), nullable=True),
    sa.Column('stats_reset', sa.DateTime(timezone=True), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pg_stat_statements_info')
    op.drop_table('pg_stat_statements')
    with op.batch_alter_table('users', schema='auth') as batch_op:
        batch_op.drop_index('users_is_anonymous_idx')
        batch_op.drop_index('users_instance_id_idx')
        batch_op.drop_index('users_instance_id_email_idx')
        batch_op.drop_index('users_email_partial_key')
        batch_op.drop_index('recovery_token_idx')
        batch_op.drop_index('reauthentication_token_idx')
        batch_op.drop_index('email_change_token_new_idx')
        batch_op.drop_index('email_change_token_current_idx')
        batch_op.drop_index('confirmation_token_idx')

    op.drop_table('users', schema='auth')
    # ### end Alembic commands ###
