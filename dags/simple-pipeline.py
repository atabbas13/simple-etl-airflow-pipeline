# Simple Pipeline
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load

def run_etl():
    raw_data = extract()
    transformed = transform(raw_data)
    load(transformed)

with DAG(
    dag_id="simple_etl_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["etl"],
) as dag:
    
    etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl
    )

    etl_task
