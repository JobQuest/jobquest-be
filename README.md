
![](https://img.shields.io/badge/JobQuest-BE-success)
![](https://img.shields.io/github/issues/JobQuest/jobquest-be?style=for-the-badge)
![](https://img.shields.io/github/stars/JobQuest/jobquest-be?style=for-the-badge)
![](https://img.shields.io/github/forks/JobQuest/jobquest-be?style=for-the-badge)
![](https://img.shields.io/pypi/pyversions/flask?style=for-the-badge)

![image](https://user-images.githubusercontent.com/62966396/109879954-8e72da00-7c33-11eb-840b-98511b8b696f.png)

## Table of Contents
  - [What it does](#what-it-does)
  - [How to Install JobQuest-be](#how-to-install-jobquest-be)
  - [API Contract](#api-contract)
  - [Schema](#schema)
  - [Dependencies](#dependencies)
  - [Testing](#testing)
  - [Learning Goals](#learning-goals)
  - [Licenses](#licenses)
  - [Contact](#contact)
  - [Acknowledgments](#acknowledgments)

## What it does
JobQuest is a text-based RPG-style campaign that aids in the job search process, while making it fun! A user can login or create an account to track their progress through different quests to defeat fantastical monsters. There are 3 types of quests: active, passive, and supportive. Active quests require you to perform actions such as *apply for a job* or *send out a resume* in order to conquer the beast. Passive quests will have you doing things like *update your resume* and *research potential companies* in order to triumph over evil. For supportive quests, you will be helping out friends (Guild-mates coming soon!) by completing such activities as *host a mock interview* for them or *review their solution to a coding challenge*. Once you complete an action outside the game, you will then select that option to deal damage to your demon. With each new quest level, the creatures you battle will become stronger, and therefore will be tougher to defeat. By completing every quest, you shall have taken the necessary steps to obtaining a job**.

Good luck on your journey through JobQuest!

** Disclaimer: The creators of JobQuest do not in any way guarantee employment by completing this game, and thinking so is down right silly of you.

## How to Install JobQuest-be

1. `git clone git@github.com:JobQuest/jobquest-be.git` 
2. `cd jobquest-be` 
3. Run `python3 -m venv ./venv`, then `source venv/bin/activate` to activate your virtual environment
4. Run `pip3 install -r requirements.txt` to install Python packages

next, create your databases and run your migrations 

5. `createdb jobquest_dev` & `createdb jobquest_test`
6. `export DATABASE_URL=postgresql://postgres:@localhost:5432/jobquest_dev`
7. `python3 manage.py db migrate`
8. `python3 manage.py db upgrade`

`upgrade` the test environment as well 

9. `export DATABASE_URL=postgresql://localhost:5432/jobquest_test`
10. `python3 manage.py db upgrade`

To shut off your virtual environment, run `deactivate` at a terminal where you have an active virtual environment.

## API Contract

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/4caa4199654cadbe93ae)

#### POST `/api/v1/users` 
Create New User

<img width="800" height="auto" alt="Create new user" src="https://user-images.githubusercontent.com/65981543/109872832-31bef180-7c2a-11eb-96f3-b43fd3d49e70.png">

#### GET `/api/v1/users`

<img width="800" height="auto" alt="GET All Users" src="https://user-images.githubusercontent.com/65981543/109875037-24573680-7c2d-11eb-8d70-8ec76e78fe94.png">

#### POST `/api/v1/users` 
Get User by Email

<img width="800" height="auto" alt="Create user by email" src="https://user-images.githubusercontent.com/65981543/109875137-494ba980-7c2d-11eb-8c90-b42c9d881223.png">

#### Unsuccessful Response: with no email in the db:

<img width="800" height="auto" alt="Screen Shot 2021-02-25 at 8 14 59 PM" src="https://user-images.githubusercontent.com/62966396/109250112-4f153b00-77a6-11eb-9990-55d93512b4bd.png">

#### GET `/api/v1/users/1/quests/completion_status=false`

<img width="800" height="auto" alt="User Uncompleted Quests" src="https://user-images.githubusercontent.com/62966396/109189596-6d9d1700-7751-11eb-9fd9-937d3a214627.png">


#### GET `/api/v1/users/1/quests/completion_status=true`

<img width="800" height="auto" alt="User Completed Quests" src="https://user-images.githubusercontent.com/62966396/109190060-f1570380-7751-11eb-936f-e4dab1b3892e.png">


#### PATCH `/api/v1/users/1/quests`

<img width="800" height="auto" alt="Update User Quests" src="https://user-images.githubusercontent.com/62966396/109201856-8ca2a580-775f-11eb-8b6f-eb59eb5e76c4.png">


#### GET `/api/v1/quests/1/encounters?progress=1`

<img width="800" height="auto" alt="Get All Encounters for a Quest by Progress" src="https://user-images.githubusercontent.com/65981543/109874922-fd990000-7c2c-11eb-8967-ee67ff3288b9.png">

## Schema

![Screen Shot 2021-02-25 at 10 51 19 AM](https://user-images.githubusercontent.com/62966396/109195377-ac35d000-7757-11eb-9753-31148d771b35.png)

## Dependencies
To install dependencies, run `pip install -r requirements.txt`
- Flask v.1.1.2
- Flask-RESTful v.0.3.8
- Flask-SQLAlchemy v.2.4.4
- psycopg2-binary v.2.8.6
- SQLAlchemy v.1.3.19
- flask_migrate v.2.5.3
- Flask-Cors v.3.0.9
- bleach v.3.2.1
- flask-script v.2.0.6
- pytest v.6.1.0
- coverage v.5.3
- gunicorn v.20.0.4
- pep8 v.1.7.1
- pycodestyle v.2.6.0
- peewee v.3.14.1


## Testing
Testing coverage sits at 98%

To run tests, ensure you are in your virtual environment and that it is the `test` environment
1. `export DATABASE_URL=postgresql://localhost:5432/jobquest_test`
2. Run `pytest`

Make sure that your enviornment variable is set to `testing`. This is done by running `env`. Check that your `DATABASE_URL` is set to the `jobquest_test` database. `DATABASE_URL=postgresql://localhost:5432/jobquest_test`

Run `pytest` in the terminal to see that all tests are passing. As of the current status there are 48 passing tests. Current code coverage is 98%

## Learning Goals

* Ultimately, demonstrate knowledge you’ve gained throughout Turing
* Use an agile process to turn well defined requirements into deployed and production ready software
* Gain experience dividing applications into components and domains of responsibilities to facilitate multi-developer teams. Service oriented architecture concepts and patterns are highly encouraged.
* Explore and implement new concepts, patterns, or libraries that have not been explicitly taught while at Turing
* Practice an advanced, professional git workflow (see whole-team expectations)
* Gain more experience using continuous integration tools to build and automate the deployment of features in various environments
* Build applications that execute in development, test, CI, and production environments
* Focus on communication between front-end and back-end teams in order to complete and deploy features that have been outlined by the project spec

## Contact

These are the contributors with whom without their imagination, hardwork and dedication this project would not have happened. We are all really excited to talk more about our project with you! Feel free to reach out to us!

<img src="https://avatars.githubusercontent.com/u/60277914?v=4" alt="Curtis Bartell"
 width="100" height="auto" />

#### Curtis Bartell: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/curtis-bartell/), [📬](mailto:cbartell980@gmail.com), [GitHub](https://github.com/c-bartell)

<img src="https://avatars.githubusercontent.com/u/4582791?v=4v" alt="Shaunda Cunningham"
 width="100" height="auto" />

#### Shaunda Cunningham: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/shaunda-cunningham/), [📬](mailto:shaunda.cunningham@gmail.com), [GitHub](https://github.com/smcunning)

<img src="https://avatars.githubusercontent.com/u/36242106?v=4" alt="Caleb Cyphers"
 width="100" height="auto" />

#### Caleb Cyphers:  [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/caleb-cyphers/), [📬](mailto:caleb.j.cyphers@gmail.com), [GitHub](https://github.com/CalebCyphers)

<img src="https://avatars.githubusercontent.com/u/60531761?v=4" alt="Jake Heft"
 width="100" height="auto" />

#### Jake Heft: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/jakeheft/), [📬](mailto:Jakeheft@gmail.com), [GitHub](https://github.com/jakeheft)

<img src="https://avatars.githubusercontent.com/u/65981543?v=4" alt="Carson Jardine"
 width="100" height="auto" />

#### Carson Jardine: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/carson-jardine/), [📬](mailto:carsonjardine@gmail.com), [GitHub](https://github.com/carson-jardine)

<img src="https://avatars0.githubusercontent.com/u/66269306?s=400&u=b59f8ccc1002269319d952aa028ee270629b2ead&v=4" alt="Olga Morgan"
 width="100" height="auto" />

#### Olga Morgan: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/olgamorgan/), [📬](mailto:olga.morgan17@gmail.com), [GitHub](https://github.com/scripka)

<img src="https://avatars.githubusercontent.com/u/62966396?v=4" alt="George Soderholm"
 width="100" height="auto" />
 
#### George Soderholm: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/george-soderholm-05776947/), [📬](mailto:georgesoderholm@gmail.com), [GitHub](https://github.com/GeorgieGirl24)


## Acknowledgments

Credits: [Ian Douglas](https://github.com/iandouglas/flask-restful-travis-heroku)

<!-- MARKDOWN LINKS -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[gITHub-sheild]: https://image.flaticon.com/icons/png/512/25/25231.png
[gitHub-sheild]: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
[github-shield]: https://www.google.com/url?sa=i&url=https%3A%2F%2Flogos-world.net%2Fgithub-logo%2F&psig=AOvVaw2iwK08oBZ-3qkYGs4YpZ1N&ust=1614092676032000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKDrvPbh_e4CFQAAAAAdAAAAABAD
