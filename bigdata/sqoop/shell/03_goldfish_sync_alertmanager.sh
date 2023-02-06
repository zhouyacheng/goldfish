#!/bin/bash
/usr/bin/sqoop import \
--connect jdbc:mysql://node02:3306/codebox?userSSL=false \
--username xxx \
--password xxx \
--table alertmanager_alertmanager \
--columns id,project_id,receiver,job,fingerprint,status,alertname,instance,description,summary,severity,groupkey,start_time,end_time \
--hive-import \
--hive-overwrite \
--hive-database goldfish_ods \
--hive-table alertmanager \
--fields-terminated-by '\t' \
-m 1
