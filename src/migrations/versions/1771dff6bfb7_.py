"""empty message

Revision ID: 1771dff6bfb7
Revises: 255d248c2517
Create Date: 2022-11-21 08:45:48.701283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1771dff6bfb7'
down_revision = '255d248c2517'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###