"""empty message

Revision ID: d6b6a94d540e
Revises: c0f1b7082238
Create Date: 2021-08-28 01:05:11.965205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6b6a94d540e'
down_revision = 'c0f1b7082238'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('work_plans_works',
    sa.Column('work_plan_id', sa.Integer(), nullable=True),
    sa.Column('work_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['work_id'], ['work.id'], ),
    sa.ForeignKeyConstraint(['work_plan_id'], ['work_plan.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('work_plans_works')
    # ### end Alembic commands ###
