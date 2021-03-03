
![](https://img.shields.io/badge/JobQuest-BE-success)

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

## Learning Goals

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
