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
    id = Column(Integer, primary_key=True, autoincrement=True)
    # unique username
    username = Column(String(80), unique=True, nullable=False)
    # unique email
    email = Column(String(100), unique=True, nullable=False)
    # xp
    xp = Column(Integer, nullable=False)
    # created_at
    created_at = Column(DateTime, default=datetime.utcnow)
    # updated_at
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # relationships
    user_quests = db.relationship('UserQuest', backref='user_quest.id', lazy='dynamic')

    def __init__(self, username, email, xp, user_id=None):
        if username is not None:
            username = bleach.clean(username).strip()
            if username == '':
                username = None

        if email is not None:
            email = bleach.clean(email).strip()
            if email == '':
                email = None

        self.username = username
        self.email = email
        self.xp = xp
        # self.created_at = created_at
        # self.updated_at = updated_at

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


    def update(self):
        """
        updates a new model into a database
        the model must exist in the database
        """
        db.session.commit()

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


    def update(self):
        """
        updates a new model into a database
        the model must exist in the database
        """
        db.session.commit()


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
