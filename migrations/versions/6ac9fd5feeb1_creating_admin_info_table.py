"""Creating admin_info table

Revision ID: 6ac9fd5feeb1
Revises: c2f0f74945f1
Create Date: 2023-09-03 00:10:46.134089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ac9fd5feeb1'
down_revision = 'c2f0f74945f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('admin_info', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_admin_info_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin_info', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_admin_info_username'))

    op.drop_table('admin_info')
    # ### end Alembic commands ###
