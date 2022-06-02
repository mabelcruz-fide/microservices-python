"""first commit

Revision ID: a2db03bd6484
Revises: 92f24b8927ec
Create Date: 2021-12-11 16:03:53.328790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2db03bd6484'
down_revision = '92f24b8927ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('detail_invoice',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('invoice_id', sa.String(), nullable=True),
    sa.Column('food_id', sa.String(), nullable=True),
    sa.Column('total', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_detail_invoice_id'), 'detail_invoice', ['id'], unique=False)
    op.create_index(op.f('ix_detail_invoice_invoice_id'), 'detail_invoice', ['invoice_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_detail_invoice_invoice_id'), table_name='detail_invoice')
    op.drop_index(op.f('ix_detail_invoice_id'), table_name='detail_invoice')
    op.drop_table('detail_invoice')
    # ### end Alembic commands ###