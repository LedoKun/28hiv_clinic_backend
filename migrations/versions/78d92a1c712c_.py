"""empty message

Revision ID: 78d92a1c712c
Revises: 1082b74911ad
Create Date: 2019-07-08 06:02:18.845722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78d92a1c712c'
down_revision = '1082b74911ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column('address', sa.Unicode(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patient', 'address')
    # ### end Alembic commands ###
