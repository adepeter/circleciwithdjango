#!/bin/bash
useradd --create-home shopwithcircleci
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable
python manage.py loaddata moove_apps/fixtures/*.json
python manage.py collectstatic --noinput
cp /usr/src/app/supervisor.conf /etc/supervisor/conf.d/
cp /usr/src/app/nginx.conf /etc/nginx/conf.d/default.conf
# rm -rf /etc/nginx/conf.d
# cp -R /usr/src/app/nginx/confs/* /etc/nginx
# nginx -c /etc/nginx/nginx.conf
# nginx -s reload
supervisord -n
# uwsgi uwsgi.ini --master --chmod-socket=666
