"""empty message

Revision ID: 80e3e44897c8
Revises: 5991db2cb3de
Create Date: 2021-02-20 19:36:39.013158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80e3e44897c8'
down_revision = '5991db2cb3de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quest_encounters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quest_id', sa.Integer(), nullable=False, foreign_key='quest.id'),
    sa.Column('type', sa.String(length=80), nullable=False),
    sa.Column('encounter_id', sa.Integer(), nullable=False, foreign_key='encounter.id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quest_encounters')
    # ### end Alembic commands ###
