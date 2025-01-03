"""update_model_order_product

Revision ID: ea7c8aab898e
Revises: 
Create Date: 2025-01-03 23:21:05.331431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea7c8aab898e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('esm_product',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('model_no', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('country_origin', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model_no')
    )
    op.create_table('esm_user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('profile', sa.String(), nullable=False),
    sa.Column('permission', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('esm_order',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('product_id', sa.UUID(), nullable=False),
    sa.Column('product_price', sa.Float(), nullable=False),
    sa.Column('product_qty', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['esm_product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('esm_order')
    op.drop_table('esm_user')
    op.drop_table('esm_product')
    # ### end Alembic commands ###