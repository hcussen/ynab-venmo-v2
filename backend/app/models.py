from typing import List, Optional

from sqlalchemy import BigInteger, Boolean, CheckConstraint, Column, Computed, Date, DateTime, Double, Enum, ForeignKeyConstraint, Index, Integer, Numeric, PrimaryKeyConstraint, SmallInteger, String, Table, Text, UniqueConstraint, Uuid, text
from sqlalchemy.dialects.postgresql import JSONB, OID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import uuid

class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        CheckConstraint('email_change_confirm_status >= 0 AND email_change_confirm_status <= 2', name='users_email_change_confirm_status_check'),
        PrimaryKeyConstraint('id', name='users_pkey'),
        UniqueConstraint('phone', name='users_phone_key'),
        Index('confirmation_token_idx', 'confirmation_token', unique=True),
        Index('email_change_token_current_idx', 'email_change_token_current', unique=True),
        Index('email_change_token_new_idx', 'email_change_token_new', unique=True),
        Index('reauthentication_token_idx', 'reauthentication_token', unique=True),
        Index('recovery_token_idx', 'recovery_token', unique=True),
        Index('users_email_partial_key', 'email', unique=True),
        Index('users_instance_id_email_idx', 'instance_id'),
        Index('users_instance_id_idx', 'instance_id'),
        Index('users_is_anonymous_idx', 'is_anonymous'),
        {'comment': 'Auth: Stores user login data within a secure schema.',
     'schema': 'auth'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    is_sso_user: Mapped[bool] = mapped_column(Boolean, server_default=text('false'), comment='Auth: Set this column to true when the account comes from SSO. These accounts can have duplicate emails.')
    is_anonymous: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    instance_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    aud: Mapped[Optional[str]] = mapped_column(String(255))
    role: Mapped[Optional[str]] = mapped_column(String(255))
    email: Mapped[Optional[str]] = mapped_column(String(255))
    encrypted_password: Mapped[Optional[str]] = mapped_column(String(255))
    email_confirmed_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    invited_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    confirmation_token: Mapped[Optional[str]] = mapped_column(String(255))
    confirmation_sent_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    recovery_token: Mapped[Optional[str]] = mapped_column(String(255))
    recovery_sent_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    email_change_token_new: Mapped[Optional[str]] = mapped_column(String(255))
    email_change: Mapped[Optional[str]] = mapped_column(String(255))
    email_change_sent_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    last_sign_in_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    raw_app_meta_data: Mapped[Optional[dict]] = mapped_column(JSONB)
    raw_user_meta_data: Mapped[Optional[dict]] = mapped_column(JSONB)
    is_super_admin: Mapped[Optional[bool]] = mapped_column(Boolean)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    phone: Mapped[Optional[str]] = mapped_column(Text, server_default=text('NULL::character varying'))
    phone_confirmed_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    phone_change: Mapped[Optional[str]] = mapped_column(Text, server_default=text("''::character varying"))
    phone_change_token: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("''::character varying"))
    phone_change_sent_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    confirmed_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), Computed('LEAST(email_confirmed_at, phone_confirmed_at)', persisted=True))
    email_change_token_current: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("''::character varying"))
    email_change_confirm_status: Mapped[Optional[int]] = mapped_column(SmallInteger, server_default=text('0'))
    banned_until: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    reauthentication_token: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("''::character varying"))
    reauthentication_sent_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))


class Notes(Base):
    __tablename__ = 'notes'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='notes_pkey'),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    title: Mapped[Optional[str]] = mapped_column(Text)


t_pg_stat_statements = Table(
    'pg_stat_statements', Base.metadata,
    Column('userid', OID),
    Column('dbid', OID),
    Column('toplevel', Boolean),
    Column('queryid', BigInteger),
    Column('query', Text),
    Column('plans', BigInteger),
    Column('total_plan_time', Double(53)),
    Column('min_plan_time', Double(53)),
    Column('max_plan_time', Double(53)),
    Column('mean_plan_time', Double(53)),
    Column('stddev_plan_time', Double(53)),
    Column('calls', BigInteger),
    Column('total_exec_time', Double(53)),
    Column('min_exec_time', Double(53)),
    Column('max_exec_time', Double(53)),
    Column('mean_exec_time', Double(53)),
    Column('stddev_exec_time', Double(53)),
    Column('rows', BigInteger),
    Column('shared_blks_hit', BigInteger),
    Column('shared_blks_read', BigInteger),
    Column('shared_blks_dirtied', BigInteger),
    Column('shared_blks_written', BigInteger),
    Column('local_blks_hit', BigInteger),
    Column('local_blks_read', BigInteger),
    Column('local_blks_dirtied', BigInteger),
    Column('local_blks_written', BigInteger),
    Column('temp_blks_read', BigInteger),
    Column('temp_blks_written', BigInteger),
    Column('blk_read_time', Double(53)),
    Column('blk_write_time', Double(53)),
    Column('temp_blk_read_time', Double(53)),
    Column('temp_blk_write_time', Double(53)),
    Column('wal_records', BigInteger),
    Column('wal_fpi', BigInteger),
    Column('wal_bytes', Numeric),
    Column('jit_functions', BigInteger),
    Column('jit_generation_time', Double(53)),
    Column('jit_inlining_count', BigInteger),
    Column('jit_inlining_time', Double(53)),
    Column('jit_optimization_count', BigInteger),
    Column('jit_optimization_time', Double(53)),
    Column('jit_emission_count', BigInteger),
    Column('jit_emission_time', Double(53))
)


t_pg_stat_statements_info = Table(
    'pg_stat_statements_info', Base.metadata,
    Column('dealloc', BigInteger),
    Column('stats_reset', DateTime(True))
)


class Planets(Base):
    __tablename__ = 'planets'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='planets_pkey'),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(Text)


class Profiles(Users):
    __tablename__ = 'profiles'
    __table_args__ = (
        ForeignKeyConstraint(['id'], ['auth.users.id'], ondelete='CASCADE', name='profiles_id_fkey'),
        PrimaryKeyConstraint('id', name='profiles_pkey')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    email_slug: Mapped[str] = mapped_column(String)
    ynab_access_token: Mapped[Optional[str]] = mapped_column(String)
    ynab_budget_id: Mapped[Optional[str]] = mapped_column(String)
    ynab_account_id: Mapped[Optional[str]] = mapped_column(String)

    transactions: Mapped[List['Transactions']] = relationship('Transactions', back_populates='profile')


class Transactions(Base):
    __tablename__ = 'transactions'
    __table_args__ = (
        ForeignKeyConstraint(['profile_id'], ['profiles.id'], ondelete='CASCADE', name='transactions_profile_id_fkey'),
        PrimaryKeyConstraint('id', name='transactions_pkey'),
        Index('idx_transactions_profile_id', 'profile_id')
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    profile_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    posted_to_ynab: Mapped[str] = mapped_column(Enum('not_posted', 'posted_success', 'posted_error', name='posting_status'), server_default=text("'not_posted'::posting_status"))
    transaction_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    amount: Mapped[Optional[int]] = mapped_column(Integer)
    payee_name: Mapped[Optional[str]] = mapped_column(String)
    memo: Mapped[Optional[str]] = mapped_column(String)
    cleared: Mapped[Optional[bool]] = mapped_column(Boolean)

    profile: Mapped['Profiles'] = relationship('Profiles', back_populates='transactions')
    post_to_ynab_errors: Mapped[List['PostToYnabErrors']] = relationship('PostToYnabErrors', back_populates='transaction')


class PostToYnabErrors(Base):
    __tablename__ = 'post_to_ynab_errors'
    __table_args__ = (
        ForeignKeyConstraint(['transaction_id'], ['transactions.id'], name='post_to_ynab_errors_transaction_id_fkey'),
        PrimaryKeyConstraint('error_id', name='post_to_ynab_errors_pkey')
    )

    error_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    transaction_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    error_timestamp: Mapped[datetime.datetime] = mapped_column(DateTime(True), server_default=text('now()'))
    error_message: Mapped[str] = mapped_column(Text)
    error_code: Mapped[Optional[str]] = mapped_column(String(50))
    error_details: Mapped[Optional[dict]] = mapped_column(JSONB)
    resolved: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('false'))

    transaction: Mapped['Transactions'] = relationship('Transactions', back_populates='post_to_ynab_errors')
