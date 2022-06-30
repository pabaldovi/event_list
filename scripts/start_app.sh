#!/bin/bash

./scripts/lint.sh
./scripts/setup_app/add_seed_data.sh
python manage.py runserver 0.0.0.0:"$PORT" # Docker requires 0.0.0.0