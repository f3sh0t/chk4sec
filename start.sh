#!/bin/bash
export BASE_URL=http://localhost
docker-compose up -d --build
docker-compose run back migrate
docker-compose run back loaddata
docker-compose run back collectstatic
docker-compose exec back ./manage.py create_super_user --username admin --password admin
