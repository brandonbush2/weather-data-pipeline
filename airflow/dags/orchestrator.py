from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.standard.operators.python import PythonOperator
import sys

sys.path.append("/opt/airflow/utils")

def safe_main_callable():
    from utils.insert_records import main
    return main()

default_args = {
    "description": "A DAG to orchestrate data",
    "start_date": datetime(2025,3,16),
    "catchup": False
}

dag = DAG(
    dag_id = "weather-api-orchestrator",
    default_args = default_args,
    schedule = timedelta(minutes = 5)
)

with dag:
    task1 = PythonOperator(
        task_id = "ingest_data_task",
        python_callable= safe_main_callable
    )
    #task2