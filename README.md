
![](https://img.shields.io/badge/JobQuest-BE-success)
![](https://img.shields.io/github/issues/JobQuest/jobquest-be?style=for-the-badge)
![](https://img.shields.io/github/stars/JobQuest/jobquest-be?style=for-the-badge)
![](https://img.shields.io/github/forks/JobQuest/jobquest-be?style=for-the-badge)
![](https://img.shields.io/pypi/pyversions/flask?style=for-the-badge)

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

## How to Install JobQuest-be

1. `git clone git@github.com:JobQuest/jobquest-be.git` 
2. `cd jobquest-be` 
3. Run `python3 -m venv ./venv`, then `source venv/bin/activate` to activate your virtual environment
4. Run `pip3 install -r requirements.txt` to install Python packages

next, create your databases and run your migrations 

5. `createdb jobquest_dev` & `createdb jobquest_test`
6. `export DATABASE_URL=postgresql://localhost:5432/jobquest_dev`
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

## Testing
Testing coverage sits at 98%

To run tests, ensure you are in your virtual environment and that it is the `test` environment
1. `export DATABASE_URL=postgresql://localhost:5432/jobquest_test`
2. Run `pytest`

## Learning Goals

## Licenses

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
[![GitHubLogo][gitHub-sheild]](https://github.com/carson-jardine)

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
