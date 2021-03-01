import bleach
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from datetime import datetime
from api import db

class Encounter(db.Model):
    """
    Encounter Model
    """
    __tablename__ = 'encounters'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True, autoincrement=True)
    # monster_image
    monster_image = Column(String(3000), nullable=False)
    # quest_id
    quest_id = Column(Integer, ForeignKey('quests.id'), index=True, nullable=False)
    # progress
    progress = Column(Integer, default=1, nullable=False)
    # created_at
    created_at = Column(DateTime, default=datetime.utcnow)
    # updated_at
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # relationships
    actions = db.relationship('Action', backref='action', lazy='dynamic')

    def __init__(self, monster_image, quest_id, progress):
        if monster_image is not None:
            monster_image = bleach.clean(monster_image).strip()
            if monster_image == '':
                monster_image = None

        self.monster_image = monster_image
        self.quest_id = quest_id
        self.progress = progress

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        """
        updates a new model into a database
        the model must exist in the database
        """
        db.session.commit()
