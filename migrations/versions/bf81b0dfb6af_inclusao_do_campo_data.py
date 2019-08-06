"""Inclusao do campo data

Revision ID: bf81b0dfb6af
Revises: bc86fbb3c312
Create Date: 2019-08-01 22:33:01.763289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf81b0dfb6af'
down_revision = 'bc86fbb3c312'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agendamentos', sa.Column('data', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('agendamentos', 'data')
    # ### end Alembic commands ###
