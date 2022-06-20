# Riverdale-Springs


## Project Description

### A Neighborhood community websites that alllows users to views posts from their neighborhoods.View Announcements,Business contacts and other neighborhood details.
### Users can also register,login and create Acconts.

## Getting Started

- Create a repository on Github.
- Create a new directory in the terminal and initialize it
- Open your choice editor and start creating your code.
- When you are done with the project,deploy it to Heroku.
- Host your Heroku link as your live link on your created Github repository.


![Optional Text](/static/pic/Screenshot_2022-06-20_23-31-16.png)


## Prerequisites

- Python3
- Django
- virtual environment

### User story
- User can create an account
- User can log in /Log out of their accounts
- User can view business contacts
- User can view neighborhood posts
- User can view their profile,
- User can create  accounts 
- Search for neighborhoods 

![Optional Text](/static/pic/Screenshot_2022-06-20_23-31-38.png)




## Deployment
### Heroku url  - https://riverdale2001.herokuapp.com/


## Deployment
- log in to heroku
```
heroku login
```
- create heroku app
```
heroku create app
```
- Upload requirements
```
pip freeze
```
- create a postgres addon to your heroku app
```
heroku addons:create heroku-postgresql:hobby-dev
```
- push to heroku

```
git push heroku master
```
- run migrations
```
heroku run python manage.py migrate
```
## Contact Information
- For any inqueries feel free to write to me through :
  - (betty.weru@student.moringaschool.com)

## Licence
- MIT License
- Copyright (c) 2022 Betty Weru
