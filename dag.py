from datetime import timedelta,datetime
from pathlib import Path
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'Ezebou',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

dag = DAG(
    dag_id='dag_Bash_Python_Operators',
    default_args=default_args,
    description='Dag para consumir api de linea de colectivos',
    start_date=datetime(2024, 3, 8 ),
    schedule_interval='@daily'
)

task1 = BashOperator(
task_id='Hola_task_1',
    bash_command='empieza'
)

task2 = PythonOperator(
    task_id='cargando_datos',
    python_callable=conectando_a_redshift,
    dag=ingestion_dag,
)

task1 << task2
