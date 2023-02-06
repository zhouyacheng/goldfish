#!/bin/bash
/usr/bin/sqoop import \
--connect jdbc:mysql://node02:3306/codebox?userSSL=false \
--username xxx \
--password xxx \
--table auth_user \
--columns id,username,first_name,email \
--hive-import \
--hive-overwrite \
--hive-database goldfish_ods \
--hive-table user \
--fields-terminated-by '\t' \
-m 1