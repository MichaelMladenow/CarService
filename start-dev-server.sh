#!/usr/bin/env sh

ps -ef | grep python | awk '{print $2}' | xargs kill -9
ps -ef | grep npm | awk '{print $2}' | xargs kill -9

python CarService/manage.py runserver &
npm run dev &
