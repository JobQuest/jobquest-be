from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api import create_app, db
from api.database.models import User, Quest, UserQuest, Encounter, Action
from tests import db_drop_everything

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

    # seed anything here we might need

    # users
    ian = User(username='iandouglas', email='ian.douglas@iandouglas.com', timestamp='2021-01-18 02:20:35.356331')
    shaunda = User(username='shaunda', email='shaunda@example.com', timestamp='2021-01-18 02:20:35.356331')
    olga = User(username='olga', email='olga@example.com', timestamp='2021-01-18 02:20:35.356331')
    caleb = User(username='caleb', email='caleb@example.com', timestamp='2021-01-18 02:20:35.356331')
    curtis = User(username='curtis', email='curtis@example.com', timestamp='2021-01-18 02:20:35.356331')
    jake = User(username='jake', email='jake@example.com', timestamp='2021-01-18 02:20:35.356331')
    carson = User(username='carson', email='carson@example.com', timestamp='2021-01-18 02:20:35.356331')
    george = User(username='george', email='george@example.com', timestamp='2021-01-18 02:20:35.356331')

    # quests
    catch_troll = Quest(name='Catch a Troll for the Town Wizard', xp=200, encounter_req=1, type='active', timestamp='2021-01-18 02:20:35.356331')
    root_bandit = Quest(name='Root out the Craghook Bandits', xp=500, encounter_req=3, type='active', timestamp='2021-01-18 02:20:35.356331')
    slay_dragon = Quest(name='Slay Argoroth the Dragon', xp=1000, encounter_req=5, type='active', timestamp='2021-01-18 02:20:35.356331')

    # user_quests
    user_quest_1 = UserQuest(quest_id=1, user_id=1, completion_status=False, progress=1, timestamp='2021-01-18 02:20:35.356331')
    user_quest_2 = UserQuest(quest_id=2, user_id=3, completion_status=False, progress=1, timestamp='2021-01-18 02:20:35.356331')
    user_quest_3 = UserQuest(quest_id=2, user_id=6, completion_status=False, progress=1, timestamp='2021-01-18 02:20:35.356331')

    # encounters
    set_troll_bait = Encounter(description='Set Troll Bait', type='active', monster_image='https://images.huffingtonpost.com/2015-02-05-trollersTroll-thumb.jpg', quest_id=1, timestamp='2021-01-18 02:20:35.356331')
    build_troll_trap = Encounter(description='Build Troll Trap', type='active', monster_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdIfSV09BWeNuPejZM4txwTFJJKikYV_WMLg&usqp=CAU', quest_id=1, timestamp='2021-01-18 02:20:35.356331')
    knock_out = Encounter(description='Knock Out the Troll', type='active', monster_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdIfSV09BWeNuPejZM4txwTFJJKikYV_WMLg&usqp=CAU', quest_id=2, timestamp='2021-01-18 02:20:35.356331')

    # actions
    leave_steak = Action(type='active', encounter_id=3,  title='Leave a Raw Steak', description='Send a message to a recruiter', timestamp='2021-01-18 02:20:35.356331')
    hit_troll_with_stick = Action(type='active', encounter_id=1, title='Hit the Troll with a Giant Stick', description='Apply to a Job', timestamp='2021-01-18 02:20:35.356331')
    hit_troll_with_stick = Action(type='active', encounter_id=1, title='Hit the Troll with a Giant Stick', description='Apply to a Job', timestamp='2021-01-18 02:20:35.356331')


    db.session.add(ian)
    db.session.add(shaunda)
    db.session.add(olga)
    db.session.add(caleb)
    db.session.add(curtis)
    db.session.add(jake)
    db.session.add(carson)
    db.session.add(george)

    db.session.add(catch_troll)
    db.session.add(root_bandit)
    db.session.add(slay_dragon)

    db.session.add(user_quest_1)
    db.session.add(user_quest_2)
    db.session.add(user_quest_3)

    db.session.add(set_troll_bait)
    db.session.add(build_troll_trap)
    db.session.add(knock_out)
    # breakpoint()
    # db.session.add(leave_steak)
    # db.session.add(hit_troll_with_stick)

    db.session.commit()
    print(f'obj count: {len(db.session.query(User).all())}')
    print(f'obj count: {len(db.session.query(Quest).all())}')
    print(f'obj count: {len(db.session.query(UserQuest).all())}')
    print(f'obj count: {len(db.session.query(Encounter).all())}')
    print(f'obj count: {len(db.session.query(Action).all())}')


if __name__ == "__main__":
    manager.run()
