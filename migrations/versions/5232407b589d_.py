"""empty message

Revision ID: 5232407b589d
Revises: cec27daf2562
Create Date: 2019-12-09 20:22:25.085504

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5232407b589d'
down_revision = 'cec27daf2562'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('agendamentos', 'periodo_fim',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_column('agendamentos', 'data')
    op.alter_column('instituicoes', 'complemento',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('instituicoes', 'nome',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('instituicoes', 'nome',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.alter_column('instituicoes', 'complemento',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.add_column('agendamentos', sa.Column('data', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.alter_column('agendamentos', 'periodo_fim',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###
