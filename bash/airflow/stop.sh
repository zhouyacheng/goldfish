#!/bin/bash
for i in `ps -ef |grep celery |grep -v grep | awk '{print $2}'`;do kill -9 $i ;done
pkill airflow