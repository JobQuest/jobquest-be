"""empty message

Revision ID: 460dfb0719c2
Revises: 6f2bd39b7fb7
Create Date: 2021-02-21 18:33:01.958961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '460dfb0719c2'
down_revision = '6f2bd39b7fb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_actions_encounter_id'), 'actions', ['encounter_id'], unique=False)
    op.create_foreign_key(None, 'actions', 'encounters', ['encounter_id'], ['id'])
    op.add_column('encounters', sa.Column('quest_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_encounters_quest_id'), 'encounters', ['quest_id'], unique=False)
    op.create_foreign_key(None, 'encounters', 'quests', ['quest_id'], ['id'])
    op.create_index(op.f('ix_quest_encounters_encounter_id'), 'quest_encounters', ['encounter_id'], unique=False)
    op.create_index(op.f('ix_quest_encounters_quest_id'), 'quest_encounters', ['quest_id'], unique=False)
    op.create_foreign_key(None, 'quest_encounters', 'encounters', ['encounter_id'], ['id'])
    op.create_foreign_key(None, 'quest_encounters', 'quests', ['quest_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'quest_encounters', type_='foreignkey')
    op.drop_constraint(None, 'quest_encounters', type_='foreignkey')
    op.drop_index(op.f('ix_quest_encounters_quest_id'), table_name='quest_encounters')
    op.drop_index(op.f('ix_quest_encounters_encounter_id'), table_name='quest_encounters')
    op.drop_constraint(None, 'encounters', type_='foreignkey')
    op.drop_index(op.f('ix_encounters_quest_id'), table_name='encounters')
    op.drop_column('encounters', 'quest_id')
    op.drop_constraint(None, 'actions', type_='foreignkey')
    op.drop_index(op.f('ix_actions_encounter_id'), table_name='actions')
    # ### end Alembic commands ###
