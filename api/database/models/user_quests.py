import bleach
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from datetime import datetime
from api import db

class UserQuest(db.Model):
    """
    UserQuest Model
    """
    __tablename__ = 'user_quests'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True, autoincrement=True)
    # quest_id, foreign_key to the quest table
    quest_id = Column(Integer, ForeignKey('quests.id'), primary_key=True)
    # user_id, foreign_key to the user table
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    # completion_status
    completion_status = Column(Boolean, nullable=False)
    # progress
    progress = Column(Integer, default=1, nullable=False)
    # created_at
    created_at = Column(DateTime, default=datetime.utcnow)
    # updated_at
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # relationships
    users = db.relationship('User', backref='user')
    quests = db.relationship('Quest', backref='quest')

    def __init__(self, quest_id, user_id, completion_status, progress):
        self.quest_id = quest_id
        self.user_id = user_id
        self.completion_status = completion_status
        self.progress = progress

    def insert(self):
        """
        inserts a new model into a database
        the model must have a unique username
        the model must have a unique id or null id
        """
        db.session.add(self)
        db.session.commit()

    def update(self):
        """
        updates a new model into a database
        the model must exist in the database
        """
        db.session.commit()
