"""empty message

Revision ID: e92246b53b8a
Revises: 7b58618eba87
Create Date: 2023-04-18 14:05:13.616308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e92246b53b8a'
down_revision = '7b58618eba87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_create', sa.DateTime(), nullable=True))

    with op.batch_alter_table('lawyer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_create', sa.DateTime(), nullable=True))

    with op.batch_alter_table('lawyer_review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lawyer_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('text', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('data_create', sa.DateTime(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'lawyer', ['lawyer_id'], ['id'])

    with op.batch_alter_table('lawyer_review_comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_lawyer_review', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('id_user', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('text', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('data_create', sa.DateTime(), nullable=True))
        batch_op.create_foreign_key(None, 'lawyer_review', ['id_lawyer_review'], ['id'])
        batch_op.create_foreign_key(None, 'user', ['id_user'], ['id'])

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lawyer_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('text', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('data_create', sa.DateTime(), nullable=True))
        batch_op.create_foreign_key(None, 'lawyer', ['lawyer_id'], ['id'])
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    with op.batch_alter_table('question_comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_question', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('id_user', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('text', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('data_create', sa.DateTime(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['id_user'], ['id'])
        batch_op.create_foreign_key(None, 'question', ['id_question'], ['id'])

    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('text', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('data_create', sa.DateTime(), nullable=True))

    with op.batch_alter_table('review_comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('text', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('data_create', sa.DateTime(), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_create', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('data_create')

    with op.batch_alter_table('review_comment', schema=None) as batch_op:
        batch_op.drop_column('data_create')
        batch_op.drop_column('text')

    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_column('data_create')
        batch_op.drop_column('text')
        batch_op.drop_column('rating')

    with op.batch_alter_table('question_comment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('data_create')
        batch_op.drop_column('text')
        batch_op.drop_column('id_user')
        batch_op.drop_column('id_question')

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('data_create')
        batch_op.drop_column('text')
        batch_op.drop_column('user_id')
        batch_op.drop_column('lawyer_id')

    with op.batch_alter_table('lawyer_review_comment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('data_create')
        batch_op.drop_column('text')
        batch_op.drop_column('id_user')
        batch_op.drop_column('id_lawyer_review')

    with op.batch_alter_table('lawyer_review', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('data_create')
        batch_op.drop_column('text')
        batch_op.drop_column('rating')
        batch_op.drop_column('user_id')
        batch_op.drop_column('lawyer_id')

    with op.batch_alter_table('lawyer', schema=None) as batch_op:
        batch_op.drop_column('data_create')

    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.drop_column('data_create')

    # ### end Alembic commands ###