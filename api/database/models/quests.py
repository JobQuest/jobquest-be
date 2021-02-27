import bleach
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from datetime import datetime
from api import db

class Quest(db.Model):
    """
    Quest Model
    """
    __tablename__ = 'quests'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True, autoincrement=True)
    # unique name
    name = Column(String(80), nullable=False)
    # xp
    xp = Column(Integer, nullable=False)
    # encounter_req
    encounter_req = Column(Integer, nullable=False)
    # type
    type = Column(String(80), nullable=False)
    # level
    level = Column(Integer, nullable=False)
    # created_at
    created_at = Column(DateTime, default=datetime.utcnow)
    # updated_at
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # relationships
    user_quests = db.relationship('UserQuest', backref='user_quest', lazy='dynamic')
    encounters = db.relationship('Encounter', backref='encounters', lazy='dynamic')

    def __init__(self, name, xp, encounter_req, type, level):
        if name is not None:
            name = bleach.clean(name).strip()
            if name == '':
                name = None

        if type is not None:
            type = bleach.clean(type).strip()
            if type == '':
                type = None

        self.name = name
        self.xp = xp
        self.encounter_req = encounter_req
        self.type = type
        self.level = level
