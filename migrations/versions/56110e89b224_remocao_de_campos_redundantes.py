"""Remocao de campos redundantes

Revision ID: 56110e89b224
Revises: bf81b0dfb6af
Create Date: 2019-08-01 22:39:01.679221

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '56110e89b224'
down_revision = 'bf81b0dfb6af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.add_column('agendamentos', sa.Column('periodoFim', sa.DateTime(), nullable=True))
    #op.add_column('agendamentos', sa.Column('periodoInicio', sa.DateTime(), nullable=True))
    #op.alter_column('usuarios', 'nome',
     #          existing_type=sa.VARCHAR(length=100),
      #         nullable=False)
    op.alter_column('agendamentos', 'periodo_fim',
               existing_type=sa.DateTime(),
               nullable=True)
    #op.drop_column('agendamentos', 'minuto_inicio')
    #op.drop_column('agendamentos', 'horario_inicio')
    #op.drop_column('agendamentos', 'horario_fim')
    #op.drop_column('agendamentos', 'data')
    #op.drop_column('agendamentos', 'minuto_fim')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agendamentos', sa.Column('minuto_fim', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('agendamentos', sa.Column('data', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('agendamentos', sa.Column('horario_fim', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('agendamentos', sa.Column('horario_inicio', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('agendamentos', sa.Column('minuto_inicio', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('agendamentos', 'periodoInicio')
    op.drop_column('agendamentos', 'periodoFim')
    # ### end Alembic commands ###
