from airflow import DAG
from airflow.models import Variable
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

PATH_DATA_DL = Variable.get("PATH_DATA_DL")


with DAG(
    dag_id="create_view_client_email_marketing",
    description="Cria uma view com resumo de \
    clientes por tipo de e-mail marketing",
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    template_searchpath="/opt/airflow/sql",
    tags=["sql", "postgres", "view"],
) as dag:

    create_view_client_email_marketing = PostgresOperator(
        task_id="create_view_client_email_marketing",
        postgres_conn_id=PATH_DATA_DL,
        # Realiza a leitura do arquivo SQL e executa o comando contido nele
        # O arquivo SQL deve estar na pasta /opt/airflow/sql
        sql="extract_client_email_marketing.sql",
    )
