#!/bin/sh
python manage.py test --verbosity 2
python manage.py runserver 0.0.0.0:8000
