#!/bin/bash

# This script migrates the database

python manage.py makemigrations events
python manage.py migrate