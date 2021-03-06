from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api import create_app, db
from api.database.models.users import User
from api.database.models.quests import Quest
from api.database.models.user_quests import UserQuest
from api.database.models.encounters import Encounter
from api.database.models.actions import Action
from tests import db_drop_everything

import csv
import psycopg2
import os
import urllib.parse as urlparse

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)

# manage migrations
manager.add_command('db', MigrateCommand)


@manager.command
def routes():
    print(app.url_map)


@manager.command
def db_seed():
    db_drop_everything(db)
    db.create_all()

    #users
    ian = User(username='iandouglas', email='ian.douglas@iandouglas.com', xp=0)
    shaunda = User(username='shaunda', email='shaunda@example.com', xp=0)
    olga = User(username='olga', email='olga@example.com', xp=0)
    caleb = User(username='caleb', email='caleb@example.com', xp=0)
    curtis = User(username='curtis', email='curtis@example.com', xp=0)
    jake = User(username='jake', email='jake@example.com', xp=0)
    carson = User(username='carson', email='carson@example.com', xp=0)
    george = User(username='george', email='george@example.com', xp=0)

    #quests
    url = urlparse.urlparse(os.environ.get('DATABASE_URL'))
    dbname = url.path[1:]
    host = url.hostname
    user = url.username
    password = url.password
    conn = psycopg2.connect(f"host={host} dbname={dbname} user={user} password={password}")
    cur = conn.cursor()
    with open('./data/quests.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute(
            "INSERT INTO quests VALUES(%s, %s, %s, %s, %s, %s)",
            row
        )
    conn.commit()

    #encounters
    conn = psycopg2.connect(f"host={host} dbname={dbname} user={user} password={password}")
    cur = conn.cursor()
    with open('./data/encounters.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute(
            "INSERT INTO encounters VALUES(%s, %s, %s, %s)",
            row
        )
    conn.commit()

    #actions
    conn = psycopg2.connect(f"host={host} dbname={dbname} user={user} password={password}")
    cur = conn.cursor()
    with open('./data/actions.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute(
            "INSERT INTO actions VALUES(%s, %s, %s)",
            row
        )
    conn.commit()

    db.session.add(ian)
    db.session.add(shaunda)
    db.session.add(olga)
    db.session.add(caleb)
    db.session.add(curtis)
    db.session.add(jake)
    db.session.add(carson)
    db.session.add(george)
    db.session.commit()

    print(f'obj count: {len(db.session.query(User).all())}')
    print(f'obj count: {len(db.session.query(Quest).all())}')
    print(f'obj count: {len(db.session.query(UserQuest).all())}')
    print(f'obj count: {len(db.session.query(Encounter).all())}')
    print(f'obj count: {len(db.session.query(Action).all())}')

if __name__ == "__main__":
    manager.run()
