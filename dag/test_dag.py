from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
import dag_config
from alert import failure_callback,success_callback,retry_callback

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['841603636@qq.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
    "on_failure_callback": failure_callback,
    "on_success_callback": success_callback,
    "on_retry_callback": retry_callback,
}

with DAG(
    'test_dag',
    default_args=default_args,
    description='test_dag',
    schedule_interval=timedelta(days=1),
    start_date=pendulum.datetime(int(dag_config.run_date[:4]), int(dag_config.run_date[-4:-2]), int(dag_config.run_date[-2:]), tz="Asia/Shanghai"),
    tags=['test_dag'],
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='echo',
        depends_on_past=False,
        bash_command='echo hello world',
        retries=1,
    )


    t3 = BashOperator(
        task_id='exit',
        bash_command="exit 0",
    )

    t4 = BashOperator(
        task_id='exit_1',
        bash_command="exit 1",
    )
    t1 >> [t2, t3,] >> t4