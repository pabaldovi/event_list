#!/bin/bash

# This script adds seed data
# https://en.wikipedia.org/wiki/Database_seeding

./manage.py flush --no-input
./manage.py loaddata events/seeds.yaml