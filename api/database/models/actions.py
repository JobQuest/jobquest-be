import bleach
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from datetime import datetime
from api import db

class Action(db.Model):
    """
    Action Model
    """
    __tablename__ = 'actions'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True, autoincrement=True)
    # encounter_id, foreign_key to the quest table
    encounter_id = Column(Integer, ForeignKey('encounters.id'), index=True, nullable=False)
    # description
    description = Column(String(400), nullable=False)
    # created_at
    created_at = Column(DateTime, default=datetime.utcnow)
    # updated_at
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, encounter_id, description):
        if description is not None:
            description = bleach.clean(description).strip()
            if description == '':
                description = None

        self.description = description
        self.encounter_id = encounter_id
