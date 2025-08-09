from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
from pipeline.main import run_pipeline


with DAG(
    dag_id="world_happiness",
    start_date=datetime(2025, 8, 9),
    schedule="@daily",
    catchup=False,
) as dag:
    run_etl = PythonOperator(
        task_id="run_world_happiness_etl",
        python_callable=run_pipeline,
    )
