# Django Webinar - Build a Todo App with me!

## This Webinar on YouTube

![Watch the Video!](https://youtu.be/VOIeDYYYqns)

## What the project looks like

![Image of the project you'll build](./TodoListApp.png)

## The Database

#### Only 1 Table (model or class in django) called Todo

| id  | title  | content        | created_at | priority |
| --- | ------ | -------------- | ---------- | -------- |
| 1   | Todo 1 | Todo 1 Content | Date time  | 1        |
| 2   | Todo 2 | Todo 2 Content | Date time  | 2        |
| 3   | Todo 3 | Todo 3 Content | Date time  | 3        |
| 4   | Todo 4 | Todo 4 Content | Date time  | 1        |

## Functionalities

- `GET` - fetches all tasks present in the database and displays them according to their priority field
- `ADD` - creates a new todo task and inserts it in the database
- `DELETE` - Removes a specific task from the database

## Steps to replicate this project

1. Virtual environment - https://docs.python.org/3/library/venv.html
2. Install sqlite3 - https://www.servermania.com/kb/articles/install-sqlite/
3. Create a virtual environment - `python3 -m venv /path/to/new/virtual/environment`
4. Activate it
   - In Terminal - `source <venv>/bin/activate`
   - In cmd.exe - `<venv>\Scripts\activate.bat`
5. Install Django via pip. Run command `pip3 install django` or `pip install django==<major>.<minor>.<patch>`.
6. Push the dependencies / python-packages into the requirements.txt `pip3 freeze > requirements.txt`
7. To Start project, run `django-admin startproject <project-name>`
8. `cd <project-name>` and then run `python3 manage.py runserver` and have a look at the basic welcome screen
9. Create app todos - `python3 manage.py startapp <app-name>`
10. Install app in settings.py and add routing to app in urls.py
11. Basic hello world Http response view in todos app
12. Add Urls in app
13. Hello world test
14. Create super user - `python3 manage.py createsuperuser`
15. Django admin tour
16. Create models
17. make migrations - `python3 manage.py makemigrations`
18. migrate - `python3 manage.py migrate`
19. Register model
20. Django admin tour
21. Python shell DB tour - `python3 manage.py shell`
22. Create template to get the data and show todos, render template in views.py
23. Create/delete todos and show changes
24. Create add todo form in template
25. make add function in views.py
26. Change urls.py
27. Show add functionality and database changes
28. Create delete todo form in template
29. make delete function in views.py
30. Change urls.py
31. Show delete functionality and db changes
32. Create Priority lists in templates

For the Webinar:
`<project-name>` = todolist

`<app-name>` = todos
