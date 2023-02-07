#!/bin/bash
source /etc/profile

for i in `ps -ef |grep celery |grep -v grep | awk '{print $2}'`;do kill -9 $i ;done
pkill airflow

airflow webserver -p 8080 -D
airflow scheduler -D
airflow celery worker -D