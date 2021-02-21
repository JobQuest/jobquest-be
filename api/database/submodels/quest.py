import bleach
from sqlalchemy import Column, String, Integer
from api import db

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

        # if user_id is not None:
        #     self.id = user_id

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
