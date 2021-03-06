"""add many fields

Revision ID: 12dd21616e80
Revises: 9f041ec7eb09
Create Date: 2020-11-02 13:39:15.155072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12dd21616e80'
down_revision = '9f041ec7eb09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('warehouse_products', sa.Column('reserve', sa.Integer(), nullable=False))
    op.alter_column('warehouse_products', 'balance',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('warehouse_products', 'name',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column('warehouse_products', 'sku',
               existing_type=sa.VARCHAR(length=15),
               nullable=False)
    op.create_index(op.f('ix_warehouse_products_name'), 'warehouse_products', ['name'], unique=False)
    op.create_index(op.f('ix_warehouse_products_sku'), 'warehouse_products', ['sku'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_warehouse_products_sku'), table_name='warehouse_products')
    op.drop_index(op.f('ix_warehouse_products_name'), table_name='warehouse_products')
    op.alter_column('warehouse_products', 'sku',
               existing_type=sa.VARCHAR(length=15),
               nullable=True)
    op.alter_column('warehouse_products', 'name',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.alter_column('warehouse_products', 'balance',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('warehouse_products', 'reserve')
    # ### end Alembic commands ###
