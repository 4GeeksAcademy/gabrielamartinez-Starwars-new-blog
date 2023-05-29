"""empty message

Revision ID: d4f77a980766
Revises: 
Create Date: 2023-05-27 09:12:56.025227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4f77a980766'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('farmer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('sur_name', sa.String(length=50), nullable=False),
    sa.Column('country', sa.String(length=40), nullable=False),
    sa.Column('ccaa', sa.String(length=40), nullable=False),
    sa.Column('company', sa.String(length=50), nullable=True),
    sa.Column('pac_num', sa.String(length=150), nullable=True),
    sa.Column('user_owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_owner'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pac_num')
    )
    op.create_table('technician',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('sur_name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=40), nullable=False),
    sa.Column('ccaa', sa.String(length=40), nullable=False),
    sa.Column('speciality', sa.String(length=120), nullable=False),
    sa.Column('num_ropo', sa.Integer(), nullable=True),
    sa.Column('user_owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_owner'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('num_ropo'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('crop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dimension_ha', sa.Integer(), nullable=False),
    sa.Column('crop_type', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('farmer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['farmer_id'], ['farmer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('farmer_id', sa.Integer(), nullable=False),
    sa.Column('technician_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=250), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('sender_role', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['farmer_id'], ['farmer.id'], ),
    sa.ForeignKeyConstraint(['technician_id'], ['technician.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=250), nullable=True),
    sa.Column('date', sa.String(length=10), nullable=True),
    sa.Column('id_farmer', sa.Integer(), nullable=True),
    sa.Column('id_technician', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_farmer'], ['farmer.id'], ),
    sa.ForeignKeyConstraint(['id_technician'], ['technician.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('id_technician', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_technician'], ['technician.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_technician'),
    sa.UniqueConstraint('name')
    )
    op.create_table('hiring',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('crop_id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('farmer_id', sa.Integer(), nullable=False),
    sa.Column('technician_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=15), nullable=False),
    sa.ForeignKeyConstraint(['crop_id'], ['crop.id'], ),
    sa.ForeignKeyConstraint(['farmer_id'], ['farmer.id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.ForeignKeyConstraint(['technician_id'], ['technician.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hiring')
    op.drop_table('service')
    op.drop_table('review')
    op.drop_table('message')
    op.drop_table('crop')
    op.drop_table('technician')
    op.drop_table('farmer')
    op.drop_table('user')
    # ### end Alembic commands ###