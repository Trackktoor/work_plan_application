"""empty message

Revision ID: bee970b6a137
Revises: 839f4d7207d7
Create Date: 2021-08-29 23:33:13.815840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bee970b6a137'
down_revision = '839f4d7207d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'work_plan', ['title'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'work_plan', type_='unique')
    # ### end Alembic commands ###
