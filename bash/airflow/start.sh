#!/bin/bash
source /etc/profile

airflow webserver -p 8080 -D
airflow scheduler -D
airflow celery worker -D
