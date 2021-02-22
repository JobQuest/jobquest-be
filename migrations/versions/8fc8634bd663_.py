"""empty message

Revision ID: 8fc8634bd663
Revises: 460dfb0719c2
Create Date: 2021-02-21 20:57:33.318578

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8fc8634bd663'
down_revision = '460dfb0719c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_quest_encounters_encounter_id', table_name='quest_encounters')
    op.drop_index('ix_quest_encounters_quest_id', table_name='quest_encounters')
    op.drop_index('ix_quest_encounters_timestamp', table_name='quest_encounters')
    op.drop_table('quest_encounters')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quest_encounters',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('quest_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('encounter_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['encounter_id'], ['encounters.id'], name='quest_encounters_encounter_id_fkey'),
    sa.ForeignKeyConstraint(['quest_id'], ['quests.id'], name='quest_encounters_quest_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='quest_encounters_pkey')
    )
    op.create_index('ix_quest_encounters_timestamp', 'quest_encounters', ['timestamp'], unique=False)
    op.create_index('ix_quest_encounters_quest_id', 'quest_encounters', ['quest_id'], unique=False)
    op.create_index('ix_quest_encounters_encounter_id', 'quest_encounters', ['encounter_id'], unique=False)
    # ### end Alembic commands ###
