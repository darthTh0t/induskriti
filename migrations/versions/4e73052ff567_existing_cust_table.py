"""existing cust_table

Revision ID: 4e73052ff567
Revises: 3a66e81cb508
Create Date: 2023-09-01 20:13:53.131663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e73052ff567'
down_revision = '3a66e81cb508'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testimonials')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testimonials',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('customer_name', sa.VARCHAR(length=30), nullable=True),
    sa.Column('testi_text', sa.TEXT(), nullable=True),
    sa.Column('rating', sa.FLOAT(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
