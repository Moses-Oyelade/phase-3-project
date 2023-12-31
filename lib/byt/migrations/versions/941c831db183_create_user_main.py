"""Create user main

Revision ID: 941c831db183
Revises: 
Create Date: 2023-10-25 14:17:54.191602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '941c831db183'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('areas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('duty', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_areas_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_equipments_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipments')
    op.drop_table('areas')
    op.drop_table('users')
    # ### end Alembic commands ###
