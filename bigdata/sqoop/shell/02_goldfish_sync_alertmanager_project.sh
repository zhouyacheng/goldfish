#!/bin/bash
/usr/bin/sqoop import \
--connect jdbc:mysql://node02:3306/codebox?userSSL=false \
--username xxx \
--password xxx \
--table alertmanager_project \
--columns id,name,role,user_id \
--hive-import \
--hive-overwrite \
--hive-database goldfish_ods \
--hive-table alertmanager_project \
--fields-terminated-by '\t' \
-m 1
