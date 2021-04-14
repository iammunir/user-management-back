# User Management

## API Documentation

API specification can be found [here](https://documenter.getpostman.com/view/10439292/TzJpiKsb)

## Prerequisites

- Make sure you have MySQL Server installed on your machine
- Create a database `mysql> CREATE DATABASE user_manag`
- Setup your setting.py file `usermanagement/usermanagement/settings.py`

```json
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'user_manag',
        'HOST': 'mysql_host',
        'PORT': 'mysql_port',
        'USER': 'mysql_username',
        'PASSWORD': 'mysql_password',
    }
}
```

## Install packages

Run `pip3 install pipenv` to install pipenv, a virtual environment tool
Run `pipenv synch` to install all packages required
Run `pipenv shell` to run virtualenv Pipfile

## Migrations

Change directory to `cd usermanagement`
Run `python3 manage.py makemigrations`
Run `python3 manage.py migrate`

## Run server

Run `python3 manage.py runserver`
