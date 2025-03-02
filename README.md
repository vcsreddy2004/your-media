# Your Media – A Social Media Platform
## Overview
Your Media is a social media platform that allows users to create, share, and interact with posts.It offers real-time updates, user authentication, and a rich text editor for enhanced post creation.

## Key Features

- `User Authentication` – Sign up, log in, and secure access with JWT.
- `Post Creation` – Users can write, edit, and delete posts.
- `Rich Text Editor` – Integrated CKEditor for enhanced post formatting.
- `Image` – Users can attach media to their posts.

# Getting Started with Create Django App
Follow these steps to set up and run the project.
# Prerequisites
Before running project, ensure you have installed python

If not download from [here](https://www.python.org/downloads/).
# Project Setup

1) First you need to create virtualenv for this project, as `virtualenv` is used to create isolated Python environments,
allowing you to manage dependencies separately for each project. This prevents conflicts between different projects that might require different versions of the same package.

  to install virtualenv use command.
```
pip install virtualenv
```
2) Create the virtualenv by the fallowing command.
```
virtualenv <your_environment_name>
```
`NOTE`:- environment name must not contains white spaces.

3) You find folder name with your environment name.Copy the folder and paste inside the project folder which you have downloaded.

4) Activate Virtualenv by fallowing command. Take command one by one do not forget to use your environment name in place of `<your_environment_name>`
```
cd <your_environment_name>
cd scripts
activate
```
5) Run `cd..` two time in order to get into the main project folder.
6) Run the fallowing command to install dependencies
```
pip install -r requirements.txt
```
7) Finnaly run the fallowing command to start project.
```
python manage.py runserver
```
Finally done. You have successfully run the project.

Here are some images of the project.
![django project 1](https://github.com/user-attachments/assets/611c7c41-388f-4b46-9141-82d2667029cc)
![django project 2](https://github.com/user-attachments/assets/660a090a-574c-4120-9d93-39ced6861dbd)
