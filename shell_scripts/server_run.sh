#!/bin/bash

./shell_scripts/wait-for-it.sh -t 120 db:3306 -- echo "mysql is up"

python manage.py makemigrations

python manage.py migrate

python manage.py runserver 0.0.0.0:8000