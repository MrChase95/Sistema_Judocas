# Sistema Judocas

Sistema de controle de uma academia de Judo

## How to Install

### Windows

`python3 -m venv venv` \
`venv\Scripts\activate.bat` \
`cd judo_app` \
`pip install -r requirements.txt`

### Linux/Mac OS

`python3 -m venv venv` \
`source venv/bin/activate` \
`cd judo_app` \
`pip install -r requirements.txt`

## How to Start the Server

`python manage.py makemigrations` \
`python manage.py migrate` \
`python manage.py runserver`

## How to Update Requirements.txt file

`pip freeze > requirements.txt`

## How to Access Register API

`home/swagger-ui/`
