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
    ian = User(username='iandouglas', email='ian.douglas@iandouglas.com', xp=0)
    shaunda = User(username='shaunda', email='shaunda@example.com', xp=300)
    olga = User(username='olga', email='olga@example.com', xp=400)
    caleb = User(username='caleb', email='caleb@example.com', xp=150)
    curtis = User(username='curtis', email='curtis@example.com', xp=2000)
    jake = User(username='jake', email='jake@example.com', xp=700)
    carson = User(username='carson', email='carson@example.com', xp=550)
    george = User(username='george', email='george@example.com', xp=900)
    #
    # # quests
    catch_troll = Quest(name='Catch a Troll for the Town Wizard', xp=200, encounter_req=1, type='active', level=1)
    root_bandit = Quest(name='Root out the Craghook Bandits', xp=500, encounter_req=3, type='active', level=2)
    slay_dragon = Quest(name='Slay Argoroth the Dragon', xp=1000, encounter_req=5, type='active', level=3)
    quest_4 = Quest(name='quest4', xp=100, encounter_req=1, type='passive', level=1)
    quest_5 = Quest(name='quest5', xp=500, encounter_req=3, type='passive', level=2)
    quest_6 = Quest(name='quest6', xp=1000, encounter_req=5, type='passive', level=3)
    kill_the_wildabeast = Quest(name="Kill the Wildabeast", xp=200, encounter_req=1, type='supportive', level=1)
    #
    # # user_quests
    user_quest_1 = UserQuest(quest_id=1, user_id=1, completion_status=False, progress=1)
    user_quest_2 = UserQuest(quest_id=2, user_id=2, completion_status=False, progress=2)
    user_quest_3 = UserQuest(quest_id=3, user_id=3, completion_status=False, progress=1)
    #
    # # encounters
    set_troll_bait = Encounter(monster_image='https://images.huffingtonpost.com/2015-02-05-trollersTroll-thumb.jpg', quest_id=1, progress=1)
    build_troll_trap = Encounter(monster_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdIfSV09BWeNuPejZM4txwTFJJKikYV_WMLg&usqp=CAU', quest_id=1, progress=1)
    knock_out = Encounter(monster_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdIfSV09BWeNuPejZM4txwTFJJKikYV_WMLg&usqp=CAU', quest_id=2, progress=1)
    trap = Encounter(monster_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdIfSV09BWeNuPejZM4txwTFJJKikYV_WMLg&usqp=CAU', quest_id=7, progress=1)

    #
    # # actions
    leave_steak = Action(encounter_id=2,  description='Send a message to a recruiter')
    hit_troll_with_stick = Action(encounter_id=1, description='Apply to a Job')
    throw_granade = Action(encounter_id=3, description='Schedule a coffee meetup with a target Company')
    punch = Action(encounter_id=4, description='Update your resume')
    kick = Action(encounter_id=4, description='Go to networking event')


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
    db.session.add(quest_4)
    db.session.add(quest_5)
    db.session.add(quest_6)
    db.session.add(kill_the_wildabeast)
    #
    db.session.add(user_quest_1)
    db.session.add(user_quest_2)
    db.session.add(user_quest_3)

    db.session.add(set_troll_bait)
    db.session.add(build_troll_trap)
    db.session.add(knock_out)
    db.session.add(trap)

    db.session.add(leave_steak)
    db.session.add(hit_troll_with_stick)
    db.session.add(throw_granade)
    db.session.add(punch)
    db.session.add(kick)

    db.session.commit()
    print(f'obj count: {len(db.session.query(User).all())}')
    print(f'obj count: {len(db.session.query(Quest).all())}')
    print(f'obj count: {len(db.session.query(UserQuest).all())}')
    print(f'obj count: {len(db.session.query(Encounter).all())}')
    print(f'obj count: {len(db.session.query(Action).all())}')
    #

if __name__ == "__main__":
    manager.run()
