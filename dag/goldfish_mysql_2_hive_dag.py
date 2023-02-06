import pendulum
import dag_config

from airflow.models.baseoperator import chain
from airflow.operators.bash import BashOperator

from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from alert import failure_callback,success_callback,retry_callback


default_args = {
    "owner": "goldfish",
    "run_date": dag_config.run_date,
    "email": [
        "841603636@qq.com"
    ],
    "on_failure_callback": failure_callback,
    "on_success_callback": success_callback,
    "on_retry_callback": retry_callback,
    "email_on_failure": False,
}


with DAG(
    'goldfish_mysql_2_hive',
    default_args=default_args,
    description='goldfish_mysql_2_hive',
    schedule_interval=timedelta(days=1),
    start_date=pendulum.datetime(int(dag_config.run_date[:4]), int(dag_config.run_date[-4:-2]), int(dag_config.run_date[-2:]), tz="Asia/Shanghai"),
    tags=['goldfish_mysql_2_hive'],
) as dag:

    user = BashOperator(
        task_id='user',
        bash_command="""
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
            """,
    )

    alertmanager_project = BashOperator(
        task_id='alertmanager_project',
        bash_command="""
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
            """,
    )

    alertmanager = BashOperator(
        task_id='alertmanager',
        bash_command="""
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
            """,
    )

    user >> alertmanager_project >> alertmanager