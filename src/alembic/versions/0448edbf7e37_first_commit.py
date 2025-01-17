"""first commit

Revision ID: 0448edbf7e37
Revises: 6736c5be71c8
Create Date: 2021-12-11 15:42:41.243130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0448edbf7e37'
down_revision = '6736c5be71c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('food',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_food_id'), 'food', ['id'], unique=False)
    op.create_index(op.f('ix_food_name'), 'food', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_food_name'), table_name='food')
    op.drop_index(op.f('ix_food_id'), table_name='food')
    op.drop_table('food')
    # ### end Alembic commands ###
