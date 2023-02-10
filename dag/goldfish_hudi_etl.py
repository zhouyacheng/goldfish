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
    'goldfish_hudi_etl',
    default_args=default_args,
    description='goldfish_hudi_etl',
    schedule_interval=timedelta(days=1),
    start_date=pendulum.datetime(int(dag_config.run_date[:4]), int(dag_config.run_date[-4:-2]), int(dag_config.run_date[-2:]), tz="Asia/Shanghai"),
    tags=['goldfish_hudi_etl'],
) as dag:


    hudi_auth_user_sync = BashOperator(
        task_id='hudi_auth_user_sync',
        bash_command="/root/anaconda3/envs/spark/bin/python3 /root/airflow/script/mysql_sync_2_hudi_ods/user.py"
    )

    hudi_alertmanager_project_sync = BashOperator(
        task_id='hudi_alertmanager_project_sync',
        bash_command="/root/anaconda3/envs/spark/bin/python3 /root/airflow/script/mysql_sync_2_hudi_ods/alertmanager_project.py"
    )

    hudi_alertmanager_sync = BashOperator(
        task_id='hudi_alertmanager_sync',
        bash_command="/root/anaconda3/envs/spark/bin/python3 /root/airflow/script/mysql_sync_2_hudi_ods/alertmanager.py"
    )

    goldfish_dwd_app_etl = BashOperator(
        task_id='goldfish_dwd_app_etl',
        bash_command="/root/anaconda3/envs/spark/bin/python3 /root/airflow/script/start_etl.py"
    )


    hudi_auth_user_sync >> hudi_alertmanager_project_sync >> hudi_alertmanager_sync >> goldfish_dwd_app_etl