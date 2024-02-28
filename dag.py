from datetime import timedelta,datetime
from pathlib import Path
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

import requests
import json
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

dag_path = os.getcwd()
default_args = {
    'start_date': datetime(2024,2, 27),
    'retries': 1,
    'retry_delay': timedelta(minutes=3)
}

ingestion_dag = DAG(
    dag_id='ingestion_data',
    default_args=default_args,
    description='lineas mas usadas de colectivos',
     schedule_interval=timedelta(days=1),
    catchup=False
)
