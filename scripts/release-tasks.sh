#!/bin/bash

python manage.py migrate
./scripts/setup_app/add_admin.sh
python manage.py loaddata events/seeds.yaml