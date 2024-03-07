#!/bin/bash
rm -rf /usr/src/senao/migrations/versions/
mkdir -p /usr/src/senao/migrations/versions/
python3 /usr/src/senao/manage.py reset-db-version
python3 /usr/src/senao/manage.py db migrate
python3 /usr/src/senao/manage.py db upgrade
