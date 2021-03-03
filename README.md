
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

## API Contract

### POST `/api/v1/users`

<img width="1015" alt="Screen Shot 2021-02-25 at 6 04 29 PM" src="https://user-images.githubusercontent.com/62966396/109249903-da420100-77a5-11eb-8e8b-38101978d1c8.png">

### GET `/api/v1/users`

<img width="1077" alt="Screen Shot 2021-02-25 at 6 13 31 PM" src="https://user-images.githubusercontent.com/62966396/109249645-5ab43200-77a5-11eb-9047-7e607c17f098.png">


### unsuccessful response: with no email in the db:

<img width="1083" alt="Screen Shot 2021-02-25 at 8 14 59 PM" src="https://user-images.githubusercontent.com/62966396/109250112-4f153b00-77a6-11eb-9990-55d93512b4bd.png">

### GET `/api/v1/users/1/quests/completion_status=false`

<img width="1014" alt="Screen Shot 2021-02-25 at 9 40 57 AM" src="https://user-images.githubusercontent.com/62966396/109189596-6d9d1700-7751-11eb-9fd9-937d3a214627.png">


### GET `/api/v1/users/1/quests/completion_status=true`

<img width="1014" alt="Screen Shot 2021-02-25 at 9 39 44 AM" src="https://user-images.githubusercontent.com/62966396/109190060-f1570380-7751-11eb-936f-e4dab1b3892e.png">



### PATCH `/api/v1/users/1/quests`
<img width="1017" alt="Screen Shot 2021-02-25 at 11 03 46 AM" src="https://user-images.githubusercontent.com/62966396/109201856-8ca2a580-775f-11eb-8b6f-eb59eb5e76c4.png">


### GET `/api/v1/quests/1/encounters?progress=1`
<img width="1017" alt="Screen Shot 2021-02-25 at 8 10 28 PM" src="https://user-images.githubusercontent.com/60531761/109249226-8682e800-77a4-11eb-8f06-07f48e5a0d22.png">

## Schema

![Screen Shot 2021-02-25 at 10 51 19 AM](https://user-images.githubusercontent.com/62966396/109195377-ac35d000-7757-11eb-9753-31148d771b35.png)

## Dependencies

## Testing

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

## Licenses

## Contact

These are the contributors with whom without their imagination, hardwork and dedication this project would not have happened. We are all really excited to talk more about our project with you! Feel free to reach out to us!

<img src="https://avatars.githubusercontent.com/u/4582791?v=4v" alt="Shaunda Cunningham"
 width="150" height="auto" />

#### Shaunda Cunningham: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/shaunda-cunningham/), [📬](mailto:shaunda.cunningham@gmail.com), [GitHub](https://github.com/smcunning)

<img src="https://avatars.githubusercontent.com/u/62966396?v=4" alt="George Soderholm"
 width="150" height="auto" />
 
#### George Soderholm: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/george-soderholm-05776947/), [📬](mailto:georgesoderholm@gmail.com), [GitHub](https://github.com/GeorgieGirl24)

<img src="https://avatars0.githubusercontent.com/u/66269306?s=400&u=b59f8ccc1002269319d952aa028ee270629b2ead&v=4" alt="Olga Morgan"
 width="150" height="auto" />

#### Olga Morgan: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/olgamorgan/), [📬](mailto:olga.morgan17@gmail.com), [GitHub](https://github.com/scripka)

<img src="https://avatars.githubusercontent.com/u/60531761?v=4" alt="Jake Heft"
 width="150" height="auto" />

#### Jake Heft: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/jakeheft/), [📬](mailto:Jakeheft@gmail.com), [GitHub](https://github.com/jakeheft)

<img src="https://avatars.githubusercontent.com/u/36242106?v=4" alt="Caleb Cyphers"
 width="150" height="auto" />

#### Caleb Cyphers:  [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/caleb-cyphers/), [📬](mailto:caleb.j.cyphers@gmail.com), [GitHub](https://github.com/CalebCyphers)

<img src="https://avatars.githubusercontent.com/u/60277914?v=4" alt="Curis Bartell"
 width="150" height="auto" />

#### Curtis Bartell: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/curtis-bartell/), [📬](mailto:cbartell980@gmail.com), [GitHub](https://github.com/c-bartell)

<img src="https://avatars.githubusercontent.com/u/65981543?v=4" alt="Carson Jardine"
 width="150" height="auto" />

#### Carson Jardine: [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/carson-jardine/), [📬](mailto:carsonjardine@gmail.com), [GitHub](https://github.com/carson-jardine)
[![GitHubLogo][gitHub-sheild]](https://github.com/carson-jardine)


## Acknowledgments

Credits: [Ian Douglas](https://github.com/iandouglas/flask-restful-travis-heroku)

<!-- MARKDOWN LINKS -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[gITHub-sheild]: https://image.flaticon.com/icons/png/512/25/25231.png
[gitHub-sheild]: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
[github-shield]: https://www.google.com/url?sa=i&url=https%3A%2F%2Flogos-world.net%2Fgithub-logo%2F&psig=AOvVaw2iwK08oBZ-3qkYGs4YpZ1N&ust=1614092676032000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKDrvPbh_e4CFQAAAAAdAAAAABAD
