# Hello World of Web Development

I made a article series on `REACT JS`. Which went (life is pain but no traction gained :/ ) nowhere. But I guess I'm back.

Becuase what is Frontend without a Backend. So This article series is on `Django` and this is the first project of the series.

It's a siple To-Do application built solely using `Django` and some `Bootstrap` for styling and I called it `Hello World of Web Development` because this is the first project of the series and everyone starts with a To-Do application.

- [LinkedIn](https://www.linkedin.com/in/pro-programmer/)
- [YouTube](http://www.youtube.com/@itvaya)
- [gtihub](https://github.com/RishatTalukder/learning_react)
- [Gmail](talukderrishat2@gmail.com)
- [discord](https://discord.gg/ZB495XggcF)

#### Pre-requisites

- Python installed in your system
- Basic knowledge of Python
- Basic knowledge of HTML and CSS
- Basic knowledge of Django (not mandatory but helpful)
- Basic knowledge of Command Line (Terminal)
- Basic knowledge of Databases and Table relationships (not mandatory but helpful)

# Setting up a django project

First we need to create a `virtual environment` to keep our project dependencies isolated from other projects. To do that, open your terminal and first check your version of python by running the command:

```bash
python --version # for windows
```

or

```bash
python3 --version # for mac and linux
```

I'm using python 3.11.8 so you should have at least python 3.8 or higher.

Why we need a virtual environment?

Because when we are using multiple packages in our project, we don't want to mess up with the global packages that are installed in our system. So we create a virtual environment for each project. So, that it is isolated and free from any conflicts.

Now, navigate to your desktop or any other folder of your choice where you want to create your project using the `cd` command. For example, if you want to create your project in the desktop, run the command:

```bash
cd Desktop
```

I always like to keep all my projects in my `desktop` So that it's easy to find them.

So, to create a virtual environment, run the command:

```bash
python -m venv env # for windows
```

or

```bash
python3 -m venv env # for mac and linux
```

> A environment is like a fresh/portable python installation. it works exactly like a normal python installation but it is isolated from the global python installation.

This will create a folder named `env` in your project directory. I'll assume you also navigated to your desktop before running the command. So, you should see a folder named `env` in your desktop.

Now, that we need to do to use this fresh python installation is to activate it. To do that, run the command:

```bash
.\env\Scripts\activate # for windows
```

or

```bash
source env/bin/activate # for mac and linux
```

If you see `(env)` in your terminal, that means your virtual environment is activated. Now, you can install any package in this environment without affecting the global packages.

And we are ready to start our django project.

Let's install `Django` in our virtual environment. To do that, run the command:

```bash
pip install django
```

> ALways remember to check if the virtual environment is activated before installing any package. If not, you might end up installing the package globally which is not what we want.

After running check for the version of django by running the command:

```bash
django-admin --version
```

You should see the version of django installed in your virtual environment. As of now, the latest version is `5.2.6`.

And we are ready to start.

Our setup is complete.

# Creating a Django Project

To create a django project, navigate to your project directory (if you are not already there, for me it's the desktop) and run the command:

```bash
django-admin startproject TodoApp
```

This will create a folder named `TodoApp` in your project directory. This is the root project folder.

In side the `TodoApp` folder, you will see another folder named `TodoApp` and a file named `manage.py`. The inner `TodoApp` folder is the actual project folder where all the settings and configurations are stored. The outer `TodoApp` folder is just a container for the project.

This can cause some issues sometimes. So, to avoid that and make a cleaner structure, I like to make a root project folder before hand and then create the django project inside that folder. So, let's do the cleaner way.

First make a new folder in your desktop named `DjangoToDoApp` and then copy the whole `env` folder inside the `DjangoToDoApp` folder. So, now your project structure should look like this:

```
Desktop(your project directory)
│
└───DjangoToDoApp(root project folder)
    │
    └───env(virtual environment)
```

Now navigate to the `DjangoToDoApp` folder using the command:

```bash
cd DjangoToDoApp
```

Now run the previous command to create the django project:

```bash
django-admin startproject BACKEND . # the dot at the end is important
```

> It's the same command as before but the dot at the end is important. It tells django to create the project in the current directory instead of creating a new folder.

So, Now you should see the `Backend` folder and the `manage.py` file inside the `DjangoToDoApp` folder. So, now your project structure should look like this:

```
Desktop(your project directory)
│
└───DjangoToDoApp(root project folder)
    │
    ├───env(virtual environment)
    │
    ├───BACKEND(django project folder)
    │   │
    │   ├───__init__.py
    │   ├───asgi.py
    │   ├───settings.py
    │   ├───urls.py
    │   └───wsgi.py
    │
    └───manage.py
```

Now, don't get confused with the names. Just think of `DjangoToDoApp` as the root project folder, `env` as the virtual environment, `Backend` as the django project folder and `manage.py` as the `main` file of the project.

Now, let's just Learn a bit about the files and folders that are created by default in a django project.

- `manage.py`: This is the main file of the project. It is used to run various commands like starting the development server, creating migrations, etc.
- `__init__.py`: This is an empty file that tells python that this folder is a package. We won't be needing to modify this file 99.9999% of the time.
- `asgi.py`: This is the entry point for ASGI-compatible web servers to serve your project. ASGI is the successor to WSGI and is used for handling asynchronous web applications. We won't be needing to modify this file 99.9999% of the time.
- `settings.py`: This is the main configuration file of the project. It contains all the settings and configurations of the project. We will be modifying this file `A LOT!`
- `urls.py`: This file contains all the URL patterns of the project. We will be modifying this file `A LOT!`. Maybe we will get more confused with this file than the `settings.py` file.
- `wsgi.py`: This is the entry point for WSGI-compatible web servers to serve your project. WSGI is the standard for Python web applications and is used for handling synchronous web applications. We won't be needing to modify this file 99.9999% of the time.

Now, that we have a basic understanding of the files and folders, let's run the development server to see if everything is working fine.

To do that, run the command:

```bash
python manage.py runserver # for windows, mac and linux
```

if this not working for linux or mac, try:

```bash
python3 manage.py runserver # for mac and linux
```

after running the command, you should see something like this:

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 14, 2025 - 06:55:27
Django version 5.2.6, using settings 'BACKEND.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
```

If you see this, that means everything is working fine. Now, open your browser and go to the development server address given in the terminal. In my case, it's `http://127.0.0.1:8000/`. You should see the default django welcome page.

![alt text](image.png)

If you see this, that means everything is working fine. And we are ready to make a To-Do application using django.

## Understanding the structure of a fullstack web application

Now, django has a lot of built-in features and those can get really overwhelming really fast for a beginner.

So, let's learn the structure of every fullstack web application first.

A fullstack web application has two main parts:

1. Frontend
2. Backend

The frontend is the part that the user interacts with. It is responsible for displaying the data to the user and taking input from the user. The frontend is built using HTML, CSS and JavaScript.

The backend is the part that handles the logic and data of the application. It is responsible for processing the data and sending it to the frontend. The backend is built using a server-side programming language like Python, Ruby, PHP, etc. In our case, we are using `Django` which is a web framework built using `Python`.

Backend has two main parts:

1. Server
2. Database

The server is responsible for handling the requests from the frontend and sending the appropriate response back to the frontend. In this case `Django is the server`.

So, django should be able to handle the requests from the frontend and send the appropriate response back to the frontend. To send the appropriate response back to the frontend, django needs to know what data to send. This data is stored in a database.

So, there must be a way to connect the `database` with the `server`. This is done using an `ORM` (Object Relational Mapping) built in django. The `ORM` is responsible for converting the data from the database into a format that can be understood by the server and vice versa.

![alt text](image-1.png)

Django has it's own built-in `ORM` which is really powerful and easy to use and also it supports multiple databases like `SQLite`, `PostgreSQL`, `MySQL`, etc. Also it has it's own built-in `admin panel` which gives you a GUI to interact with the database. So, you don't need to write any SQL queries to interact with the database. You can just use the `ORM` to interact with the database.

So, for now let's stick to the default database which is `SQLite`. It is a lightweight database and it is perfect for small projects like this.

If you have the development server running, you should see some errors in the terminal. This is because we have some unapplied migrations. Migrations are like version control for your database schema. They are used to keep track of the changes made to the database schema over time.

But we don't have a database yet. So, let's create the database by applying the migrations. To do that, stop the development server by pressing `CTRL + C` in the terminal and then run the command:

```bash
python manage.py migrate
```

After that run the development server again by running the command:

```bash
python manage.py runserver
```

The errors should be gone now. If you see the default django welcome page again, that means everything is working fine.

And If you take a look in your project directory, you should see a new file named `db.sqlite3`. This is the database file. This file contains all the data of your application.

> if you are using vs code, you can see the database file in the file explorer. But not whats inside the file. I use a extension named `SQLite` to view the database file.

And we have a working django project with a database setup. Now, we are ready to make a To-Do application using django.

# Creating a Django App

First we need to create a `Django App`. It's a Application template that contains all the files and folders needed to build a `specific feature` of the project.

A project can have multiple apps. For example, a blog project can have a `blog` app, a `comments` app, a `users` app, etc. Each app is responsible for a specific feature of the project.

We can make multiple apps in a django project to keep the code organized and modular. But for this project, we will only make one app named `todo`.

To create a django app, make sure you are in the project directory (for me it's `DjangoToDoApp`) and run the command:

```bash
python manage.py startapp todo
```

> By running this command, a new folder named `todo` will be created in your project directory. This is the app folder.

So, now your project structure should look like this:

```
Desktop(your project directory)
│
└───DjangoToDoApp(root project folder)
    │
    ├───env(virtual environment)
    │
    ├───BACKEND(django project folder)
    │   │
    │   ├───__init__.py
    │   ├───asgi.py
    │   ├───settings.py
    │   ├───urls.py
    │   └───wsgi.py
    │
    ├───manage.py
    │
    └───todo(django app folder)
        │
        ├───__init__.py
        ├───admin.py
        ├───apps.py
        ├───models.py
        ├───tests.py
        ├───views.py
        └───migrations
            └───__init__.py

```

In this folder, you will see some files and folders that are created by default. Let's learn about them:

- `__init__.py`: This is an empty file that tells python that this folder is a package. We won't be needing to modify this like never.
- `admin.py`: This file is used to register the models in the admin panel. We will be modifying this file later.
- `apps.py`: This file is used to configure the app. We won't be needing to modify this file like never.
- `models.py`: This file is used to define the models of the app. We will be modifying this file a lot.
- `tests.py`: This file is used to write tests for the app. We won't be needing to modify this file for now.
- `views.py`: This file is used to define the views of the app. We will be modifying this file a lot.
- `migrations`: This folder is used to store the migration files. We won't be modifying this folder at all.

Django uses the `MVC` (Model-View-Controller) architecture to build web applications. But in django, the `Controller` part is handled by the framework itself. So, we only need to worry about the `Model` and the `View` part.

## Model View Template (MVT) Architecture

This is a modern architecture used by a lot of web frameworks like `Django`, `Flask`, `Ruby on Rails`, etc. It is a variation of the `MVC` architecture.

![alt text](image-2.png)

Model refers to the `data` of the application. It is responsible for managing the data and the logic of the application. In django, the models are defined in the `models.py` file.

This is where we define the structure of the data and the relationships between the data. Which is handled by the `ORM` of django. ORMs are `Object Relational Mappers`. They are used to convert the data from the database into a format that can be understood by the server and vice versa and it is fully object oriented. So, we can interact with the database using python objects instead of writing raw SQL queries.

This model will send the data to the view when requested. View refers to the `user interface` of the application. It is responsible for displaying the data to the user and taking input from the user. In django, the views are defined in the `views.py` file. It takes handles the requests from the user and sends the appropriate response back to the user with the `Template`.

The template is the HTML file that is used to display the data to the user. It is responsible for rendering the data in a user-friendly way. In django, We will create a new folder named `templates` in the `todo` app folder to store the HTML files. but that's for later.

Also another thing that is left out is the `URL Dispatcher`. It is responsible for mapping the URLs to the views. In django, the URL dispatcher is defined in the `urls.py` file.

I hope you got a brief overview of the `MVT` architecture. We will be using this architecture to build our To-Do application.

Just remember, in a nutshell, the `Model` is responsible for managing the data which is used by the `View` to display the data to the user using the `Template` for a cirtain `URL` defined in the `URL Dispatcher`.

So, let's move on to the next step.

# Integreting the App with the Project

WHen we make a new app, we need to tell the engine(Backend) that we have a new app. So, that it can include the app in the project.

To do that, open the `settings.py` file in the `Backend` folder and then find the `INSTALLED_APPS` list. This list contains all the apps that are included in the project. By default, it contains some built-in apps like `admin`, `auth`, `contenttypes`, `sessions`, etc.

Add the name of the app that we just created to the top of the list. In our case, the name of the app is `todo`. So, add `'todo',` to the top of the list. It should look like this:

```python
# backend/settings.py
INSTALLED_APPS = [
    'todo',
    # 'todo.apps.TodoConfig',  # Optional: If you want to use the AppConfig class

    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

You can also use the method documented in the [official documentation](https://docs.djangoproject.com/en/5.2/intro/tutorial02/) to add the app to the list. In the documentation, they use the `AppConfig` class to add the app to the list. But I prefer the first method because it is simpler and easier to understand. If it doesn't work, you can always try the second method.

You should see no errors in the terminal if you have the development server running. Now we can create our first model in the `models.py` file of the `todo` app.

> We will always try to follow this rule `model -> migrate -> view -> template` when we are building a feature. This will help us to keep the code organized, modular and less error prone.

# Making the first Model

Just give you guys an example of how to make a model in django i'll make a very simple model named `Task` in the `models.py` file of the `todo` app.

So, go to the `models.py` file and you should see something like this:

```python
from django.db import models
# Create your models here.
```

> This line imports the `models` module from the `django.db` package. This module contains all the classes and functions needed to define the models in django.

We will use this module to define our model.

Now, let's define the `Task` model. A task will have a `title` and date when it was created. So, we will define two fields in the model: `title` and `created_at`.

```python
from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

```

> Here, we defined a class named `Task` that inherits from the `models.Model` class. This class represents a table in the database. Each attribute of the class represents a column in the table.

- `title`: This is a `CharField` which is used to store string data. We have set the `max_length` attribute to `200` which means the maximum length of the title can be 200 characters.
- `created_at`: This is a `DateTimeField` which is used to store date and time data. We have set the `auto_now_add` attribute to `True` which means the field will be automatically set to the current date and time when the object is created.

Some more wise words about fields in django models:

> Class(inheriting models.Model) means a table in the database.
> Attributes inside the class means columns in the table.

So, Our database Should Look like this:

- Name of the table: `task` (appname_modelname in lowercase)
  | id | title | created_at |
  |----|-------------|---------------------|
  | 1 | Sample Task | 2023-09-14 10:00:00 |

Now, that we have defined our first model, remember the rule `model -> migrate -> view -> template`, we need to create a migration for the model and then apply the migration to create the table in the database.

So, by just making the model, we haven't created the table in the database yet. We need to create a migration for the model and then apply the migration to create the table in the database.

So, let's create a migration for the model. To do that, run the command:

```bash
python manage.py makemigrations
```

After running this command, you should see something like this:

![alt text](image-3.png)

this means the backend has detected the changes made to the models of the app and we have successfully created a migration for the model.

> If this doesn't work, make sure you have added the app to the `INSTALLED_APPS` list in the `settings.py` file. In my case, it worked by directly adding the app name to the list instead of using the `AppConfig` class. If it doesn't work for you, you might have to use the `AppConfig` class to add the app to the list like I have demonstrated before.

Now, to be sure if the migration is created successfully, you can check the `migrations` folder in the `todo` app. You should see a new file named something like `0001_initial.py`. This file contains the migration for the model.

```python
# Generated by Django 5.2.6 on 2025-09-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
```

This is the migration file that is created for the `Task` model. What it does?

Open the `db.sqlite3` file using a SQLite viewer or any database management tool that supports SQLite. Trry to find the `task` table in the database. You wouldn't find it.

Django will use this file to create the table in the database when we apply the migration.

Now, we migrate.

```bash
python manage.py migrate
```

and you should see something like this:

![alt text](image-4.png)

This means the migration has been applied successfully and the table has been created in the database.

Now goto the database file and check if the table is created successfully. You should see a new table named `todo_task` in the database. This is the table that is created for the `Task` model.

Django automatically adds the app name as a prefix to the model name to create the table name to avoid any conflicts with other apps that might have the same model name.

And in the table, you should see three columns: `id`, `title` and `created_at`. The `id` column is automatically created by django as the primary key for the table.

I hope you understood all those steps. For me when I was learning django, this was sooo tough to understand. But now I can explain it in a simple way.

It's all about practice. The more you practice, the more you understand.

So, first rule: Model -> Migrate -> View -> Template

Second rule: Always `makemigrations` after any change in the models and then `migrate` to apply the changes to the database.

Now, let's talk about the `admin panel` of django.

# Django Admin Panel

Django has a nice built-in admin panel that allows you to manage the data of your application. It is a web-based interface that allows you to create, read, update and delete the data in the database.

Because we now have a table in the database, we need to add some data to be rendered on the screen. We can do that using the admin panel.

First we need to create a superuser to access the admin panel. To do that, run the command:

```bash
python manage.py createsuperuser
```

This will prompt you to enter a username, email and password for the superuser. Enter the details and press enter.

> Remember the username and password because we will need it to login to the admin panel.

Now, fo to the browser and go to the admin panel address which is `http://127.0.0.1:8000/admin/`. You should see the login page of the admin panel.

Enter the username and password that you just created and press enter. You should see the dashboard of the admin panel.

![alt text](image-5.png)

Now, you should see some options like `Users`, `Groups`, etc. These are the built-in models of django. But we don't see our `Task` model here because we haven't registered it yet.

We need to register the model in the `admin.py` file so that it can be accessed from the admin panel.

To do that, open the `admin.py` file in the `todo` app and you should see something like this:

```python
from django.contrib import admin

# Register your models here.
```

Here we can register our models. So, let's register the `Task` model. To do that, we need to import the model first. So, add the following line at the top of the file:

```python
from django.contrib import admin

# Register your models here.
from .models import Task

admin.site.register(Task)
```

Here, we imported the `Task` model from the `models.py` file and then registered it using the `admin.site.register()` method.

Now, reload the admin panel page in the browser. You should see a new option named `Tasks` in the dashboard.

You have full access to the `Task` model from the admin panel. You can create, read, update and delete the tasks from here.

> The admin panel is a powerful tool that allows you to manage the data of your application without writing any code. There are many more features in the admin panel that you can explore on your own.

Click on the `Tasks` option to go to the tasks page. You should see something like this:
![alt text](image-6.png)

The tasks page is empty because we haven't created any tasks yet. To create a new task, click on the `Add Task` button at the top right corner of the page.

You should see a form to create a new task. Enter the title of the task and click on the `Save` button at the bottom of the page.

You should see the task that you just created in the tasks page as `Task object (1)`. When you click it you should see the details of the task that you just created.

Which is great. We have successfully created our first model, made a migration for the model but one thing that I don't like is the naming of the task object. It should show the title of the task instead of `Task object (1)`, right?

This is because we haven't defined the `__str__` method in the model. This method is used to define the string representation of the object. By default, it returns the name of the class and the primary key of the object.

But we can override this method to return the title of the task instead. To do that, open the `models.py` file in the `todo` app and add the following method to the `Task` class:

```python
from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title # Override the __str__ method to return the title of the task
```

This will override the default `__str__` method and return the title of the task instead.

> These are called magic methods in python. They are used to define the behavior of the object. `__str__` is used to define the string representation of the object. And you must return something from this method. If you don't return anything, it will return `None` by default.

So, remember rule number 2?

Always `makemigrations` after any change in the models and then `migrate` to apply the changes to the database.

So, run the command:

```bash
python manage.py makemigrations
python manage.py migrate
```

Now, run the server again and go to the admin panel. You should see the title of the task instead of `Task object (1)`.

Noice.

Now, you can create more tasks from the admin panel and see them in the tasks page.

One cool thing about this is, if you take a look in the database file, you should see the tasks that you just created in the `todo_task` table.

Well, That's it for this part. We can now create, read, update and delete tasks (CRUD operations) from the admin panel. But we want to do it from the frontend, right?

Not So fast. Let's just finish up the backend part first.

Now, that we have a task title model. We should also store more information about the task right? Like it's `description`, `status` (completed or not), `priority` (high, medium, low), etc.

So, let's make a new table in the database to store this information.

# Making Detailed Task Model

To do that, we will create a new model named `TaskDetail` in the `models.py` file of the `todo` app. As this is a part of the `Task` model, we need to build a `relationship` between the two models.

If you don't know about relationships in databases, I suggest you to learn about it first. It is a very important concept in databases and you will be using it a lot when building web applications.

We will be using a `One-to-One` relationship between the `Task` and `TaskDetail` models. This means that each task can have only one task detail and each task detail can belong to only one task.

So, open the `models.py` file in the `todo` app and add the following code:

```python
class TaskDetail(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='details') # One-to-One relationship with Task model and when the task is deleted, the task detail will also be deleted
    description = models.TextField() # TextField is used to store large text data
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add is used to set the field to the current date and time when the object is created
    priority = models.IntegerField(default=1,choices=[(1,'Low'),(2,'Medium'),(3,'High')]) # IntegerField is used to store integer data and choices is used to limit the choices for the field
    completed = models.BooleanField(default=False) # BooleanField is used to store boolean data

    def __str__(self):
        return f"Detail for {self.task.title}"
```

Here, we defined a new class named `TaskDetail` that inherits from the `models.Model` class. Which represents the `taskdetail` table in the database.

- `task`: This is a `OneToOneField` field which is used to create a one-to-one relationship between the `Task` and `TaskDetail` models. We have set the `on_delete` attribute to `models.CASCADE` which means that when the `Task` object is deleted, the `TaskDetail` object will also be deleted. We have also set the `related_name` attribute to `'details'` which means that we can access the task details from the task object using `task.details`. If we don't set this attribute, django will use the default name which is `taskdetail_set`.

> The `related_name` attribute is used to specify the name of the reverse relation from the related object back to this one. In this case, it allows us to access the task details from the task object using `task.details`. If we don't set this attribute, django will use the default name which is `taskdetail_set`.

- `description`: This is a `TextField` which is used to store large text data. We will use this field to store the description of the task.
- `created_at`: This is a `DateTimeField` which is used to store date and time data. We have set the `auto_now_add` attribute to `True` which means the field will be automatically set to the current date and time when the object is created.
- `priority`: This is an `IntegerField` which is used to store integer data. We have set the `default` attribute to `1` which means the default priority of the task will be `Low`. We have also set the `choices` attribute to a list of tuples which limits the choices for the field. The first element of the tuple is the value that will be stored in the database and the second element is the human-readable name of the choice.
- `completed`: This is a `BooleanField` which is used to store boolean data. We have set the `default` attribute to `False` which means the task is not completed by default.
- `__str__` method: This method is used to define the string representation of the object. We have overridden this method to return the title of the task along with the text "Detail for".

Now, remember the rule?

Always `makemigrations` after any change in the models and then `migrate` to apply the changes to the database.

```bash
python manage.py makemigrations
python manage.py migrate
```

Now, run the server again.

Everything should be working properly. No errors in the terminal. Ignor the warnings.

Now, just like we registered the `Task` model in the `admin.py` file, we need to register the `TaskDetail` model as well.

To do that, open the `admin.py` file in the `todo` app and add the following line:

```python
from .models import Task, TaskDetail

admin.site.register(Task)
admin.site.register(TaskDetail)
```

Now, you should be able to see the `Task` model in the admin panel.

Now, we have two tables in the database: `todo_task` and `todo_taskdetail`. Add some data to the `todo_taskdetail` table and you should see it in the `todo_task` table.

![alt text](image-7.png)

> To add data you should see the some thing like this with an extra option for tasks. It's a drop down menu that has all the tasks in the database. You can select a task and then add data to it which will be stored in the `todo_taskdetail` table.

Now, that we have a working django project with a database setup. We are ready to make a To-Do application using django.

# Creating a View

Remember the rule `model -> migrate -> view -> template` when we are building a feature.

> Ps: This rule will change soon.

We made the models and the migrations. Now time to make a view.

A `view` is a function that takes some `input` and returns some `output`.

In django, a `view` is a function that takes a `request` object as input and returns a `response` object as output.

This view function will be responsible for handling the requests from the frontend and sending the appropriate response back to the frontend.

In short it takes a request finds the data from the database and sends it back to the frontend.

So, let's make a view function in the `views.py` file of the `todo` app.

Open the `views.py` file in the `todo` app and you should see something like this:

```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.core import serializers
# Create your views here.


def index(request):
    data = Task.objects.all()
    data = serializers.serialize('json', data)
    return HttpResponse(data, content_type='application/json')
```

> This view function is taking a request as input and returning a JSON response as output.

> We have to use the `serializers.serialize()` method to convert the data we get from the database to a JSON string before sending it back to the frontend.

> HttpResponse is a class that will automatically set the correct headers and status code for the response.

> This should create a JSON response with the data from the database.

So, now let's See how we can show this data in the frontend.

We have everything ready and now we have to tell django where to put this view function in the browser.

If you take a close look at the `urls.py` file in the `BACKEND` app, you will see something like this:

```python
"""
URL configuration for BACKEND project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

> The comments in the `urls.py` file has some valuable information about how we should use the `path()` function to map the URLs to the views.

This is the file where all our URLs should be defined. We will be using this file to map the URLs to the views.

AAANDDD that will change the rule to `model -> migrate -> view -> URL -> template`.

Now, let's add the path for our view function in the `urls.py` file.

Open the `urls.py` file, I'll remove the comments and add the following code:

```python
from django.contrib import admin
from django.urls import path
from todo.views import index #we have to import the view function here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), #we have to add the path for the view function here
]
```

> Here right after the `from django.urls import path` line, we have to import the view function from the `todo.views` module. Because we are going to connect the view function to the URL.

After that, we can create a new path for the view function. Byt adding the `path()` function and passing the URL as the first argument and the view function as the second argument.

> The `name` argument is optional and it is used to give a name to the URL. It can be helpful sometimes.

Here we are adding this view function to the root URL of the application.

So, if we run the server again, we should see something like this:

![alt text](image-8.png)

And we can see the data and it's format in the root URL of the application.

GREAT! We have a working django project with a database setup.

WE HAVE DONE ALL THE STEPS.

And I hope you understood all those steps well. I know it's a long process but once you get the hang of it, it's really easy.

> PS: THE HARD PART IS STILL ON IT'S WAY.

We this was the very basic building blocks of a django project.

But if we continue this path we will face some very painful problems.

So, Time to make the code a little neat and tidy.

# Making the code a little neat and tidy

First, let's follow the real advice given by the Django documentation.

NEVER, EVER, EVER, EVER, EVER, EVER use directly make `paths` of different apps in the `BACKEND/urls.py` file.

This is because it will cause a lot of problemsm confusion and conflicts.

So, we should always make a new file inside the app folder and Where we will create all the paths for all the views of the app and we can connect them to the URLs.

For example, if we want to create a path for the `index` view of the `todo` app, we should create a new file named `urls.py` inside the `todo` app folder and add the following code:

```python
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]
```

It should be `EXACTLY` as above. If there is even a single difference, it will not work.

> This the issue I will always have with Django. Sometime the typos will cause the whole project to break.

So, be careful...

> Advice: Just copy the code from the `BACKEND/urls.py` file and paste it in the new file and remove the admin panel path.

Now, let's connect the new path to the URL.

Open the `BACKEND/urls.py` file and add the following code:

```python
from django.contrib import admin
from django.urls import path, include # We have to import the include function here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]
```

Here, we have used the `include()` function to include the `urls.py` file of the `todo` app.

This will attach all the paths of the `todo` app to the root URL of the application.

You can do some experimentation by changing the path for the include function to include the `urls.py` file of any other app you have created.

Let's say we want to include the `todo` app path to the `/tasks` URL.

```python
from django.contrib import admin
from django.urls import path, include # We have to import the include function here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('todo.urls')),
]
```

Now the root URL of the application should show some error like this:
![alt text](image-9.png)

This is because we changed that path to render the url of the `todo` app from the root URL(`''`) to `/tasks`.

So, if we go to the `/tasks` URL, we should see the data and it's format in the root URL of the application.

It's best practice to set different URLs for different Apps.


Now, time to make a real Front Page.

# Making a Real Front Page with Django

We know the steps and now we can make an actual Front Page with Django.

We have evrything ready and do you remember the rule `model -> migrate -> view -> URL -> template`?

Let's setup a template in the `todo` app.

Open the `templates` folder in the `todo` app and create a new folder named `todo`. And inside that folder, create a new file named `index.html`.

YES! YOU OPEN A NEW FOLDER NAMED `templates` IN THE `todo` APP AND CREATE ANOTHER FOLDER NAMED ACCORDING TO THE APP NAME(IT HAS TO BE THE SAME AS THE APP NAME) AND INSIDE THAT FOLDER, CREATE A NEW FILE NAMED `index.html`.

> NOTE: `todo/templates/todo/index.html`

I'll tell you why we need this whacky naming convention.

JUST DO IT!

Now, let's make a template for the `index` view of the `todo` app.

Open the `index.html` file in the `todo` app and you should see something like this:

```html
<!-- todo/templates/todo/index.html -->
<h1>WELCOME!</h1>

<h2>This is the Home page of the To-Do application</h2>
```

This is the default template that is used by the `index` view of the `todo` app.

> This is the default template that is used by the `index` view of the `todo` app.

Now, we connect this template with the `index` view of the `todo` app.

> I'll comment out the previous index function and add the following code:

```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.core import serializers
# Create your views here.


# def index(request):
#     data = Task.objects.all()
#     data = serializers.serialize('json', data)
#     return HttpResponse(data, content_type='application/json')

def index(request):
    return render(request, 'todo/index.html')
```

> This is the `index` view of the `todo` app. We have added the `render()` function to render the template named `todo/index.html`.

The render function takes two arguments, the first is the request object and the second is the template name.


Now, let's run the server again and go to the root URL of the application.

![alt text](image-10.png)

And we can see the data and it's format in the root URL of the application.

Awesome!

Now let's talk about the `weird` naming convention.

## Template Naming Convention

Django projects usually have a lot of apps. And these apps has their own templates and views.

So, it can be a hassle to keep track of all the templates and views of all the apps. So, what django does is search for the template and view in the `templates` folder of the app and if it doesn't find it, it will search in the `templates` folder of the root project.

Now, this can cause some conflicts.

Let's say you have an app named `blog` and you have a template named `index.html` in the `blog` app.

And you have another app named `todo` and you have a template named `index.html` in the `todo` app.

If you run the server, you will see the `index.html` template of the `blog` app and not the `index.html` template of the `todo` app.

This is because django will search for the template in the `templates` folder of the `blog` app first and if it doesn't find it, it will search in the `templates` folder of the root project.

Why it'll search in the blog app first?

It's because we added the app to the `INSTALLED_APPS` list in the `settings.py` file of the root project.

Whatever app comes first in the `INSTALLED_APPS` list will be the first app that django will search for the template in then the next app and so on.

So, if we have multiple apps in the `INSTALLED_APPS` list and each app has a template with the same name, django will search for the template in the app that comes first in the `INSTALLED_APPS` list first.

This is the reason why we have to follow the `weird` naming convention. Which will specify the app name in the template name.

This way we can avoid any conflicts and make our code a little neat and tidy.

Now, another issue will arise.

## Template Inheritance

As you can see we can directly add html code in a template and connect a view to it. It will render the html code in the template.

But think about a normal html page. It has a lot of common code like the header, footer, navigation, etc.

These elements don't change often and they are common for all the pages.

So, how can we make a template that can be reused for other templates?

This is called `template inheritance`.

Template inheritance is a way to reuse a template and make it more generic.

For example, we can make a `base.html` template and all the other templates can inherit from it.

Here is the `base.html` template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is the base template</h1>
    {% block content %}
    <!-- This is the content block where all the content will be added -->
    {% endblock %}
</body>
</html>
```

> This is the `base.html` template. Which the structure of a standerd html page and Inside that we have a `content` block where all the content will be added.

Don't get worried about the `block` tags.

As we are using a non-standard framework, we have to write the code in a different language than `JS` in side a html file to work with it.

So, django has a built-in template language called `Jinja2` which is used to render the templates.

If you are using vs code you can install the [django extension](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django) to get syntax highlighting for the django template language.

I refer to this as `django template tags` because they are used to render the templates.

There many types of `django template tags` and we will learn about them as we move forward with the project.

Now, let's talk about the `block` tags.

The `block` tags are used to define the content block where all the content will be added when the template is inherited.

For example, we can define a `content` block in the `base.html` template and all the other templates can inherit from it.

And when they inherit from the `base.html` template, they will be able to add their content to the `content` block.

Now, a common misconception is that the `block` tags are used to define only the `content` block or we should always use the `block content` tag to define the content block.

The syntax for the `block` tags is like this:

```html
{% block title %}
    <!-- This is the content of the title block -->
{% endblock %}
```
> Here you can see the `block` tag and the `title` argument. We can put anything we want in the `title` argument and it will be used as the name of the content block.

So, we can define the `title` of the block to specify where in the base template the content of the block will be added.

Now, let's inherit this base template in our `index.html` template.

Open the `index.html` file in the `todo` app and let's extend:

```html
{% extends 'todo/base.html' %}

<h1>WELCOME!</h1>

<h2>This is the Home page of the To-Do application</h2>
```

> The extends tag is used to inherit the base template and we add the path of the base template in the `todo/base.html` file.

Now, let's run the server again and go to the root URL of the application.

![alt text](image-11.png)

Well this is interesting. The base is there but where is the index?

Well, it's because the index.html file is extending the `base.html` which makes the `index.html` a child template of the `base.html` template.

In the `base.html` template, we have a `content` block that specifies where the `content` of the child template will be added and now we have to tell django what to put in the `content` block of the `index.html` template.

So, we will add the block content tag in the `index.html` template.

```html
{% extends 'todo/base.html' %}

{% block content %}
  <h1>WELCOME!</h1>

  <h2>This is the Home page of the To-Do application</h2>
{% endblock %}
```

Now, the contents of the `index.html` template will be added to the `content` block of the `base.html` template.

![alt text](image-12.png)

A little confusing right?

> Rule 3: Always add a block for the child template and with the same name as the block of the parent template.

One last thing I want to show you guys is how we can add links to different pages in the `base.html` template.

We can add links to different pages in the `base.html` template by using the `url` tag.

For example, we can add a link to the `index` page of the `todo` app by using the following code:

```html
<a href="{% url 'index' %}">Home</a>
```

> The `url` tag is used to get the URL of the page and the `index` argument is the name of the view function of the `todo` app.

Remember we added a name attribute to the `index` view function in the `urls.py` file of the `todo` app.

```python
#todo/urls.py
from django.urls import path
from todo.views import index

urlpatterns = [
    path('', index, name='index'), #the name of the URL is index
]
```

> We use this name to get the URL of the `index` view function.

The url tag will automatically add the URL of the `index` view function to the `Home` link.

I hope you understood everything well.

Now let's see the data in the browser.

# Rendering the data in the browser

Let's talk about the `render()` function.

The `render()` function is used to render the template in the `index` view of the `todo` app.

When we are in a url the view function of that url is called and the `render()` function is used to render the template.

But it has some other uses too.

It can send a HTTP response to the browser with the data in the template.

> Simply: we can send data to the browser with the template along with the HTTP response.

So, let's see what tasks are in the database.

We will make a new page for it. And do you remember the rule `model -> migrate -> view -> URL -> template`?

We have the model for the tasks in the database. WE also migrated the database.

now we need a view function to render the template.

Let's make a new view function in the `todo` app.

Open the `views.py` file and let's make a new function named `tasks`.

```python
#todo/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.core import serializers
# Create your views here.


#everything else stays the same

def tasks(request):
    data = Task.objects.all() #we have to get the data from the database
    context = {'tasks': data} #we have to add the data to the context
    return render(request, 'todo/tasks.html', context) #we pass the context to the render function
```

> This is the `tasks` view function of the `todo` app. We have added the `render()` function to render the template named `todo/tasks.html` and we have added the data to the context.

The data will be available via the `tasks` key in the context.

So, let's make a url for the `tasks` view function.

Open the `urls.py` file and add the following code:

```python
#todo/urls.py
from django.urls import path
from todo.views import index, tasks

urlpatterns = [
    path('', index, name='index'), #the name of the URL is index
    path('tasks/', tasks, name='tasks'), #the name of the URL is topics
]
```

The url is set now time for the template.

Make a new file inside the `templates/todo` folder named `tasks.html`.

Open the `tasks.html` file and you should see something like this:

```html
<!-- todo/templates/todo/tasks.html -->
{% extends 'todo/base.html' %}

{% block content %}
  <h1>
    This is the tasks page of the To-Do application
  </h1>
{% endblock %}
```
> Here we extend the `base.html` template and inside the `content` block we have a `h1` tag with the text `This is the tasks page of the To-Do application`.

This should render correctly in the `localhost:8000/tasks/` URL.

![alt text](image-13.png)

I've some changes to the `base.html` template. I removed the `h1` tag. I want to make the base template a navigation bar for the whole application.

Let's add the a new link for the `tasks` page in the `base.html` template.

```html
<!-- todo/templates/todo/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <a href="{% url 'index' %}">Home</a>
    <a href="{% url 'tasks' %}">Tasks</a>
    {% block content %}
    <!-- This is the content block where all the content will be added -->
    {% endblock %}
</body>
</html>
```

> The `url` tag is used to get the URL of the page and the `tasks` argument is the name of the view function of the `todo` app.

Now, how do we access the data we sent to the template?

We can access the data in the template by using the `context` variable.

For example, we can access the data in the `tasks` view function by using the `context` variable.

It's pretty simple. We can render the whole context in the template by using `{{}}` which is called a `template variable`.

Inside the double curly braces, we can access the keys of the context and the values of the context.

So, let's access the `tasks` key in the context and render it in the template.

```html
<!-- todo/templates/todo/tasks.html -->
{% extends 'todo/base.html' %}

{% block content %}
  <h1>This is the tasks page of the To-Do application</h1>
  {{tasks}}
{% endblock %}
```

> Now if you reload the browser, you should see the whole data of the tasks in the database.

![alt text](image-14.png)

You can access a single key in the context by using the dot notation. Let's say I want only the `first` entry of the tasks to be rendered in the template.

I can do that by using the dot notation.

```html
<!-- todo/templates/todo/tasks.html -->
{% extends 'todo/base.html' %}

{% block content %}
  <h1>This is the tasks page of the To-Do application</h1>
  {{tasks.0}}
{% endblock %}
```

> We cannot do indexing the python way but we can do it in the template using the dot notation.

And it will render the first entry of the tasks list.

![alt text](image-15.png)

We can also access other properties of the tasks object.

For example, we can access the `title` or `created_at` property of the tasks object by using the dot notation.

```html
<!-- todo/templates/todo/tasks.html -->
{% extends 'todo/base.html' %}

{% block content %}
  <h1>This is the tasks page of the To-Do application</h1>
  {{ tasks.0.title }}
  {{ tasks.0.created_at }}
{% endblock %}

```

![alt text](image-16.png)

> Here I'm taking the `0` index of the tasks list and accessing the `title` and `created_at` property of the tasks object.

We can do a lot more that just rendering the data independently.

We can have for loops and if statements and other things.

So, let's list out all the tasks in the database.

Open the `tasks.html` file and add the following code:

```html
<!-- todo/templates/todo/tasks.html -->
{% extends 'todo/base.html' %}

{% block content %}
  <h1>This is the tasks page of the To-Do application</h1>

  {% for task in tasks %}
    <h2>{{ task.title }}</h2>
    <p>{{ task.created_at }}</p>
  {% endfor %}

{% endblock %}

```

> Here we have a for loop that loops through all the tasks in the database and renders the title and created_at of each task.

Most of the django template tags have a starting `{% %}` and an ending `{% end %}` tag.

For example, the `for` tag has a starting `{% for variable in list %}` and an ending `{% endfor %}` tag.

![alt text](image-17.png)

