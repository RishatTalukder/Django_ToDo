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

After running check for the version of django by running the command:

```bash
django-admin --version
```

You should see the version of django installed in your virtual environment. As of now, the latest version is `5.2.6`.

And we are ready to start.

