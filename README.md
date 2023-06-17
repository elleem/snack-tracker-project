## Project: Django Models

Author: Lauren Main

Version 1.0

### Links and Resources

This page references [Click if You Dare: 100 Favorite Horror Stories](https://www.npr.org/2018/08/16/632779706/click-if-you-dare-100-favorite-horror-stories)

### Overview



#### Feature

- [x] Create a project

- [x] Create an app
  
- [x] Create a model
  
  - [x] create a name CharField with max length 64 characters
  
  - [x] create a purchaser ForeignKey with CASCADE delete option
  
  - [x] create a description TextField
  
- [x] Add model to admin
  
- [x] Modify Snack model to have user-friendly display in admin

- [x] Create migrations and migrate data

- [x] Create a super user

- [x] Run dev server

- [x] add snacks via admin panel

- [x] create another user and add more snack via admin panel

- [x] confirm snacks behave as expected with model name, purchaser, and description

- [x] create SnackListView

- [x] update url patterns

- [x] update snack app urls

- [x] add detail view

- [x] update app urlpatterns to handle detail view



### Setup

initiate a virtual environment

`python3.11 -m venv .venv`

`source .venv/bin/activate`

### how to initialize/run this app

`python manage.py runserver`

run via the local server

### tests

run tests via `python manage.py test`
