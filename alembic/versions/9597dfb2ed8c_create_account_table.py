"""create account table

Revision ID: 9597dfb2ed8c
Revises: 
Create Date: 2021-08-27 17:16:40.031955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9597dfb2ed8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('tour',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('title', sa.String()),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('departure', sa.String(), nullable=True),
        sa.Column('picture', sa.String(), nullable=True),
        sa.Column('price', sa.Numeric(10, 2), nullable=True),
        sa.Column('stars', sa.Integer(), nullable=True),
        sa.Column('country', sa.String(), nullable=True),
        sa.Column('nights', sa.Integer(), nullable=True),
        sa.Column('date', sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('departure',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('title', sa.String()),
        sa.Column('abbr', sa.String(), nullable=True),
        sa.Column('tour_id', sa.Integer(), sa.ForeignKey('tour.id')),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('tour')
    op.drop_table('departure')
