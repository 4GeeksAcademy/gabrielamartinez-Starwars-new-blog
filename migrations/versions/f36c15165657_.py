"""empty message

Revision ID: f36c15165657
Revises: 254de1ea23d5
Create Date: 2023-12-11 22:10:20.964216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f36c15165657'
down_revision = '254de1ea23d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('publicacion',
    sa.Column('idPublicacion', sa.Integer(), nullable=False),
    sa.Column('idUser', sa.Integer(), nullable=True),
    sa.Column('nombre', sa.String(length=200), nullable=True),
    sa.Column('apellido', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('descripcion', sa.String(length=200), nullable=False),
    sa.Column('comuna', sa.String(length=200), nullable=False),
    sa.Column('rubro', sa.String(length=200), nullable=False),
    sa.Column('fecha', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('idPublicacion'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('fecha')
    )
    op.drop_table('user_publicacion')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_publicacion',
    sa.Column('idPublicacion', sa.INTEGER(), server_default=sa.text('nextval(\'"user_publicacion_idPublicacion_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('idUser', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nombre', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('apellido', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('descripcion', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('comuna', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('rubro', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('fecha', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('idPublicacion', name='user_publicacion_pkey'),
    sa.UniqueConstraint('email', name='user_publicacion_email_key'),
    sa.UniqueConstraint('fecha', name='user_publicacion_fecha_key')
    )
    op.drop_table('publicacion')
    # ### end Alembic commands ###