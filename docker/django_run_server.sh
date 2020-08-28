#!/bin/bash

set -xe

python manage.py makemigrations
python manage.py makemigrations api
python manage.py migrate
exec python manage.py runserver 0.0.0.0:8000
