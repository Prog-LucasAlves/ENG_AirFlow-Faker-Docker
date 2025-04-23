from airflow import DAG
from airflow.models import Variable
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

# Variável que contém o caminho do banco de dados
PATH_DATA_DL = Variable.get("PATH_DATA_DL")


with DAG(
    dag_id="create_table_cliente_email_marketing",
    description="Cria uma view com resumo de \
    clientes por tipo de e-mail marketing",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
    template_searchpath="/opt/airflow/sql",
    tags=["sql", "postgres", "table"],
) as dag:

    create_table_cliente_email_marketing = PostgresOperator(
        task_id="create_table_cliente_email_marketing",
        postgres_conn_id=PATH_DATA_DL,
        sql="extract_qtd_cliente_email_marketing.sql",
    )

with DAG(
    dag_id="create_table_cliente_ativo",
    description="Cria uma view com resumo de \
        clientes ativos",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
    template_searchpath="/opt/airflow/sql",
    tags=["sql", "postgres", "table"],
) as dag:

    create_table_cliente_ativo = PostgresOperator(
        task_id="create_table_cliente_ativo",
        postgres_conn_id=PATH_DATA_DL,
        sql="extract_cliente_ativo.sql",
    )
