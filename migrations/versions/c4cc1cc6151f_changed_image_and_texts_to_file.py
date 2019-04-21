"""changed image and texts to file

Revision ID: c4cc1cc6151f
Revises: 4fc555326eb8
Create Date: 2019-04-14 14:15:55.673014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4cc1cc6151f'
down_revision = '4fc555326eb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)

    with op.batch_alter_table('text', schema=None) as batch_op:
        batch_op.add_column(sa.Column('text', sa.String(length=200), nullable=True))
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.drop_column('file')

    with op.batch_alter_table('video', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('video', schema=None) as batch_op:
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    with op.batch_alter_table('text', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file', sa.BLOB(), nullable=True))
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.drop_column('text')

    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###
