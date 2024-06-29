#!/bin/sh
source .venv/bin/activate
python narou_reader/manage.py runserver $PORT
