#!/bin/sh

set -e # Terminates the sript if any commands fail

python manage.py wait_for_db
# Collects and stores all the static files in the static files directory
python manage.py collectstatis --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
