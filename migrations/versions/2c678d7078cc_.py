"""Primeira Migration

Revision ID: 2c678d7078cc
Revises: 
Create Date: 2019-07-13 23:18:47.689753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c678d7078cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('laboratorios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('host', sa.String(length=30), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('tempo_experimento', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('agendamentos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('horario_inicio', sa.Integer(), nullable=False),
    sa.Column('minuto_inicio', sa.Integer(), nullable=False),
    sa.Column('horario_fim', sa.Integer(), nullable=False),
    sa.Column('minuto_fim', sa.Integer(), nullable=False),
    sa.Column('observacao', sa.String(length=300), nullable=True),
    sa.Column('laboratorio_id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['laboratorio_id'], ['laboratorios.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agendamentos')
    op.drop_table('laboratorios')
    # ### end Alembic commands ###
