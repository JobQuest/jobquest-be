"""empty message

Revision ID: ad5b16b26c1c
Revises: f1f02b72493c
Create Date: 2021-02-21 12:34:18.343998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad5b16b26c1c'
down_revision = 'f1f02b72493c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actions', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_actions_timestamp'), 'actions', ['timestamp'], unique=False)
    op.add_column('encounters', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_encounters_timestamp'), 'encounters', ['timestamp'], unique=False)
    op.add_column('quest_encounters', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_quest_encounters_timestamp'), 'quest_encounters', ['timestamp'], unique=False)
    op.add_column('quests', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_quests_timestamp'), 'quests', ['timestamp'], unique=False)
    op.add_column('user_quests', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_quests_timestamp'), 'user_quests', ['timestamp'], unique=False)
    op.add_column('users', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_users_timestamp'), 'users', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_timestamp'), table_name='users')
    op.drop_column('users', 'timestamp')
    op.drop_index(op.f('ix_user_quests_timestamp'), table_name='user_quests')
    op.drop_column('user_quests', 'timestamp')
    op.drop_index(op.f('ix_quests_timestamp'), table_name='quests')
    op.drop_column('quests', 'timestamp')
    op.drop_index(op.f('ix_quest_encounters_timestamp'), table_name='quest_encounters')
    op.drop_column('quest_encounters', 'timestamp')
    op.drop_index(op.f('ix_encounters_timestamp'), table_name='encounters')
    op.drop_column('encounters', 'timestamp')
    op.drop_index(op.f('ix_actions_timestamp'), table_name='actions')
    op.drop_column('actions', 'timestamp')
    # ### end Alembic commands ###
