import bleach
from sqlalchemy import Column, String, Integer, Boolean
from api import db
# from api.database.submodels import *
# from submodels.user_quest.py import *
# from submodels.quest_encounter.py import *


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

    def __init__(self, username, email, user_id=None):
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

    def __init__(self, name, xp, encounter_req, type):
        if name is not None:
            name = bleach.clean(name).strip()
            if name == '':
                name = None

        if xp is not None:
            xp = bleach.clean(xp).strip()
            if xp == '':
                xp = None

        if encounter_req is not None:
            encounter_req = bleach.clean(encounter_req).strip()
            if encounter_req == '':
                encounter_req = None

        if type is not None:
            type = bleach.clean(type).strip()
            if type == '':
                type = None

        self.name = name
        self.xp = xp
        self.encounter_req = encounter_req
        self.type = type

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

class UserQuest(db.Model):
    """
    UserQuest Model
    """
    __tablename__ = 'user_quests'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True)
    # quest_id, foreign_key to the quest table
    quest_id = Column(Integer, foreign_key='quest.id', nullable=False)
    # user_id, foreign_key to the user table
    user_id = Column(Integer, foreign_key='user.id', nullable=False)
    # completion_status
    completion_status = Column(Boolean, nullable=False)
    # progress
    progress = Column(Integer, nullable=False)


    def __init__(self, quest_id, user_id, completion_status, progress):
        if quest_id is not None:
            quest_id = bleach.clean(quest_id).strip()
            if quest_id == '':
                quest_id = None

        if user_id is not None:
            user_id = bleach.clean(user_id).strip()
            if user_id == '':
                user_id = None

        if completion_status is not None:
            completion_status = bleach.clean(completion_status).strip()
            if completion_status == '':
                completion_status = None

        if progress is not None:
            progress = bleach.clean(progress).strip()
            if progress == '':
                progress = None

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

    def __init__(self, description, type, monster_image):
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

class QuestEncounter(db.Model):
    """
    QuestEncounter Model
    """
    __tablename__ = 'quest_encounters'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True)
    # quest_id, foreign_key to the quest table
    quest_id = Column(Integer, foreign_key='quest.id', nullable=False)
    # type
    type = Column(String(80), nullable=False)
    # encounter_id, foreign_key to the encounter table
    encounter_id = Column(Integer, foreign_key='encounter.id', nullable=False)

    def __init__(self, quest_id, type, encounter_id):
        if quest_id is not None:
            quest_id = bleach.clean(quest_id).strip()
            if quest_id == '':
                quest_id = None

        if type is not None:
            type = bleach.clean(type).strip()
            if type == '':
                type = None

        if encounter_id is not None:
            encounter_id = bleach.clean(encounter_id).strip()
            if encounter_id == '':
                encounter_id = None

        self.quest_id = quest_id
        self.type = type
        self.encounter_id = encounter_id

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

class Action(db.Model):
    """
    Action Model
    """
    __tablename__ = 'actions'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True)
    # encounter_id, foreign_key to the quest table
    encounter_id = Column(Integer, foreign_key='encounter.id', nullable=False)
    # type
    type = Column(String(80), nullable=False)
    # title
    title = Column(String(80), nullable=False)
    # description
    description = Column(String(1000), nullable=False)

    def __init__(self, title, description, type, encounter_id):
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

        if encounter_id is not None:
            encounter_id = bleach.clean(encounter_id).strip()
            if encounter_id == '':
                encounter_id = None

        self.title = title
        self.description = description
        self.type = type
        self.encounter_id = encounter_id

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
