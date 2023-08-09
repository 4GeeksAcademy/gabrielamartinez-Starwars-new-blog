"""empty message

Revision ID: b86b9220d764
Revises: 1a1f7b77152f
Create Date: 2023-08-05 21:11:01.826456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b86b9220d764'
down_revision = '1a1f7b77152f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_images', schema=None) as batch_op:
        batch_op.drop_column('order')

    # ### end Alembic commands ###