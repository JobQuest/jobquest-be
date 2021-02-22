import bleach
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from datetime import datetime
from api import db


class User(db.Model):
    """
    User Model
    """
    __tablename__ = 'users'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True)
    # unique username
    username = Column(String(80), unique=True, nullable=False)
    # unique email
    email = Column(String(100), unique=True, nullable=False)
    # time_stamp
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    # relationships
    # user_quests = db.relationship('UserQuest', backref='user_quest.id', lazy='dynamic')

    def __init__(self, username, email, timestamp, user_id=None):
        if username is not None:
            username = bleach.clean(username).strip()
            if username == '':
                username = None

        if email is not None:
            email = bleach.clean(email).strip()
            if email == '':
                email = None

        if timestamp is not None:
            timestamp = bleach.clean(timestamp).strip()
            if timestamp == '':
                timestamp = None

        self.username = username
        self.email = email
        self.timestamp = timestamp
        if user_id is not None:
            self.id = user_id

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

    def delete(self):
        """
        deletes model from database
        the model must exist in the database
        """
        db.session.delete(self)
        db.session.commit()

class Quest(db.Model):
    """
    Quest Model
    """
    __tablename__ = 'quests'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True)
    # unique name
    name = Column(String(80), nullable=False)
    # xp
    xp = Column(Integer, nullable=False)
    # encounter_req
    encounter_req = Column(Integer, nullable=False)
    # type
    type = Column(String(80), nullable=False)
    # time_stamp
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    # relationships
    # quests_encounters = db.relationship('QuestEncounter', backref='quest_encounter', lazy='dynamic')
    # user_quests = db.relationship('UserQuest', backref='user_quest', lazy='dynamic')

    def __init__(self, name, xp, encounter_req, type, timestamp):
        if name is not None:
            name = bleach.clean(name).strip()
            if name == '':
                name = None

        if type is not None:
            type = bleach.clean(type).strip()
            if type == '':
                type = None

        if timestamp is not None:
            timestamp = bleach.clean(timestamp).strip()
            if timestamp == '':
                timestamp = None

        self.name = name
        self.xp = xp
        self.encounter_req = encounter_req
        self.type = type
        self.timestamp = timestamp

    def insert(self):
        """
        inserts a new model into a database
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

    def delete(self):
        """
        deletes model from database
        the model must exist in the database
        """
        db.session.delete(self)
        db.session.commit()

class UserQuest(db.Model):
    """
    UserQuest Model
    """
    __tablename__ = 'user_quests'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True)
    # quest_id, foreign_key to the quest table
    quest_id = Column(Integer, ForeignKey('quests.id'), nullable=False)
    # user_id, foreign_key to the user table
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # completion_status
    completion_status = Column(Boolean, nullable=False)
    # progress
    progress = Column(Integer, default=1, nullable=False)
    # time_stamp
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    # relationships
    # users = db.relationship('User', backref='user', lazy='dynamic')
    # quests = db.relationship('Quest', backref='quest', lazy='dynamic')

    def __init__(self, quest_id, user_id, completion_status, progress, timestamp):

        self.quest_id = quest_id
        self.user_id = user_id
        self.completion_status = completion_status
        self.progress = progress
        self.timestamp = timestamp

    def insert(self):
        """
        inserts a new model into a database
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

    def delete(self):
        """
        deletes model from database
        the model must exist in the database
        """
        db.session.delete(self)
        db.session.commit()

class Encounter(db.Model):
    """
    Encounter Model
    """
    __tablename__ = 'encounters'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True)
    # description
    description = Column(String(1000), nullable=False)
    # type
    type = Column(String(80), nullable=False)
    # monster_image
    monster_image = Column(String(3000), nullable=False)
    # quest_id
    quest_id = Column(Integer, ForeignKey('quests.id'), nullable=False)
    # time_stamp
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    # relationships
    # actions = db.relationship('Action', backref='action', lazy='dynamic')

    def __init__(self, description, type, monster_image, quest_id, timestamp):
        if description is not None:
            description = bleach.clean(description).strip()
            if description == '':
                description = None

        if type is not None:
            type = bleach.clean(type).strip()
            if type == '':
                type = None

        if monster_image is not None:
            monster_image = bleach.clean(monster_image).strip()
            if monster_image == '':
                monster_image = None

        self.description = description
        self.type = type
        self.monster_image = monster_image
        self.quest_id = quest_id
        self.timestamp = timestamp

    def insert(self):
        """
        inserts a new model into a database
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

    def delete(self):
        """
        deletes model from database
        the model must exist in the database
        """
        db.session.delete(self)
        db.session.commit()


class Action(db.Model):
    """
    Action Model
    """
    __tablename__ = 'actions'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True)
    # encounter_id, foreign_key to the quest table
    encounter_id = Column(Integer, ForeignKey('encounters.id'), nullable=False)
    # type
    type = Column(String(80), nullable=False)
    # title
    title = Column(String(80), nullable=False)
    # description
    description = Column(String(1000), nullable=False)
    # time_stamp
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)

    def __init__(self, encounter_id, title, description, type, timestamp):
        if title is not None:
            title = bleach.clean(title).strip()
            if title == '':
                title = None

        if description is not None:
            description = bleach.clean(description).strip()
            if description == '':
                description = None

        if type is not None:
            type = bleach.clean(type).strip()
            if type == '':
                type = None

        self.title = title
        self.description = description
        self.type = type
        self.encounter_id = encounter_id
        self.timestamp = timestamp

    def insert(self):
        """
        inserts a new model into a database
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

    def delete(self):
        """
        deletes model from database
        the model must exist in the database
        """
        db.session.delete(self)
        db.session.commit()
