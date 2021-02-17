"""create basic tables

Revision ID: 969ba149a2cc
Revises: 
Create Date: 2021-02-17 05:38:18.089428

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '969ba149a2cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('last_modified', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.String(200)),
        sa.Column('code', sa.Unicode(20)),
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('last_modified', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('nickname', sa.String(50), nullable=False),
        sa.Column('name', sa.String(50), default='John Doe'),
        sa.Column('email', sa.Unicode(50), nullable=False),
        sa.Column('description', sa.String(200)),
        sa.Column('role', sa.Integer, sa.ForeignKey('roles.id')),
    )

    op.create_table(
        'events',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('last_modified', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.String(200)),
        sa.Column('code', sa.Unicode(20)),
        sa.Column('creator_id', sa.Integer, sa.ForeignKey('users.id')),
    )

    op.create_table(
        'stages',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('last_modified', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.String(200)),
        sa.Column('event_id', sa.Integer, sa.ForeignKey('events.id')),
        sa.Column('responsible', sa.Integer, sa.ForeignKey('users.id')),
    )

    op.create_table(
        'performances',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('last_modified', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.String(200)),
        sa.Column('code', sa.Unicode(20)),
        sa.Column('order', sa.Integer),
        sa.Column('duration', sa.Interval),
        sa.Column('person', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('stage', sa.Integer, sa.ForeignKey('stages.id')),
    )

    op.create_table(
        'materials',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('last_modified', sa.DateTime(timezone=False), default=datetime.now),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.String(200)),
        sa.Column('storage_url', sa.Unicode(20)),
        sa.Column('performance', sa.Integer, sa.ForeignKey('performances.id')),
    )


def downgrade():
    op.drop_table('materials')
    op.drop_table('performances')
    op.drop_table('stages')
    op.drop_table('events')
    op.drop_table('users')
    op.drop_table('roles')
