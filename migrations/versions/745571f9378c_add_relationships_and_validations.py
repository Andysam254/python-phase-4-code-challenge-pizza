"""Add relationships and validations

Revision ID: 745571f9378c
Revises: 1c4d7eb6a7ee
Create Date: 2025-01-25 13:35:46.242165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '745571f9378c'
down_revision = '1c4d7eb6a7ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('ingredients',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('restaurant_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('pizza_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_restaurant_pizzas_pizza_id_pizzas'), 'pizzas', ['pizza_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), 'restaurants', ['restaurant_id'], ['id'])

    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_restaurant_pizzas_pizza_id_pizzas'), type_='foreignkey')
        batch_op.drop_column('pizza_id')
        batch_op.drop_column('restaurant_id')

    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.alter_column('ingredients',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
