"""rename category to category_id

Revision ID: 52d5ccded6b5
Revises: 12dd21616e80
Create Date: 2020-11-02 14:55:21.674945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52d5ccded6b5'
down_revision = '12dd21616e80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('warehouse_products', sa.Column('category_id', sa.Integer(), nullable=True))
    op.drop_constraint('warehouse_products_category_fkey', 'warehouse_products', type_='foreignkey')
    op.create_foreign_key(None, 'warehouse_products', 'warehouse_category', ['category_id'], ['id'])
    op.drop_column('warehouse_products', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('warehouse_products', sa.Column('category', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'warehouse_products', type_='foreignkey')
    op.create_foreign_key('warehouse_products_category_fkey', 'warehouse_products', 'warehouse_category', ['category'], ['id'])
    op.drop_column('warehouse_products', 'category_id')
    # ### end Alembic commands ###
