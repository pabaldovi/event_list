#!/bin/bash

python manage.py migrate
python manage.py loaddata events/seeds.yaml
