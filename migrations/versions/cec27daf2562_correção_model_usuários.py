"""Correção model Usuários

Revision ID: cec27daf2562
Revises: 40457bd6281b
Create Date: 2019-08-19 20:17:30.378358

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cec27daf2562'
down_revision = '40457bd6281b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.add_column('usuarios', sa.Column('verificado', sa.Boolean(), nullable=True))
    #op.drop_column('usuarios', 'login_count')
    #op.drop_column('usuarios', 'last_login_ip')
    #op.drop_column('usuarios', 'last_login_at')
    #op.drop_column('usuarios', 'current_login_ip')
    #op.drop_column('usuarios', 'current_login_at')
    op.alter_column('usuarios', 'nome',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuarios', sa.Column('current_login_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('usuarios', sa.Column('current_login_ip', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('usuarios', sa.Column('last_login_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('usuarios', sa.Column('last_login_ip', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('usuarios', sa.Column('login_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('usuarios', 'verificado')
    # ### end Alembic commands ###
