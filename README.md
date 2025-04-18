
# 🌀 Projeto Airflow + Docker + PostgreSQL

Este projeto tem como objetivo demonstrar uma arquitetura simples e funcional para orquestração de pipelines utilizando **Apache Airflow** em conjunto com **Docker** e **PostgreSQL**. A stack é ideal para fluxos de dados programáveis, com controle total sobre agendamentos, logs e estados de execução.

**Banco de dados utlizado do Projeto [AED_DBT](https://github.com/Prog-LucasAlves/AED_DBT)**

---

## 🚀 Tecnologias Utilizadas

O projeto foi desenvolvido utilizando uma combinação poderosa de tecnologias modernas, garantindo robustez, escalabilidade e facilidade de manutenção para orquestração de pipelines de dados. Abaixo estão as principais tecnologias empregadas:

- 🔧 **Apache Airflow**
Apache Airflow é uma plataforma de código aberto usada para programar, monitorar e gerenciar workflows de dados. Neste projeto, o Airflow atua como o orquestrador principal, responsável por executar DAGs (Directed Acyclic Graphs) que representam fluxos de tarefas. Com ele, é possível definir dependências, agendamentos, monitoramento e logging de cada etapa do processo.

- 🐳 **Docker**
Docker é a base da arquitetura do projeto, permitindo empacotar todos os serviços em containers independentes e reproduzíveis. Usamos docker-compose para orquestrar múltiplos containers, facilitando a configuração, execução e escalabilidade do ambiente de desenvolvimento e produção. Isso garante que o projeto funcione de forma idêntica em qualquer máquina.

- 🐘 **PostgreSQL**
O PostgreSQL é um banco de dados relacional robusto, seguro e open source. Neste projeto, ele funciona como banco de metadados do Airflow, armazenando informações sobre DAGs, tarefas, execuções e estados. Ele também pode ser utilizado como fonte de dados em DAGs personalizadas, com consultas SQL sendo executadas diretamente a partir do Airflow.

- 📦 **Python**
A linguagem principal utilizada no desenvolvimento das DAGs e na customização do Airflow é o Python. Por meio de operadores como BashOperator, PythonOperator e PostgresOperator, é possível criar fluxos de trabalho altamente flexíveis e integrados com outras tecnologias.

- 📁 **Dockerfile e Docker Compose**
O Dockerfile define como o container do Airflow será construído, permitindo a instalação de dependências personalizadas. Já o docker-compose.yml organiza os serviços em rede (como Airflow Webserver, Scheduler e PostgreSQL), define volumes e garante que tudo seja inicializado na ordem correta, com comandos específicos para inicialização e persistência dos dados.

- 📄 **.env**
Utilizamos variáveis de ambiente através do arquivo .env para garantir flexibilidade e segurança na configuração do projeto. Isso permite separar dados sensíveis do código e facilitar mudanças sem alterar diretamente os arquivos principais.

---

## 📁 Estrutura do Projeto

```bash
airflow_project/
├── dags/                    # Arquivos com os fluxos de trabalho (DAGs)
│   └── dag_etl.py
├── sql                      # Arquivos Sql que serão executados pela (DAG)
├── .env                     # Variáveis de ambiente
├── .flake8                  # Configuração flake8
├── .gitignore               # Arquivos a serem ignorados
├── pre-commit-config.yaml   # Configuração precommit
├── .python-version          # Versão do Python utilizada no projeto
├── Dockerfile               # Imagem customizada do Airflow
├── docker-compose.yml       # Orquestração dos serviços
├── pyproject.toml           # Lista de dependências do projeto
├── README.md                # Documentação do projeto

```

---

## ⚙️ Pré-requisitos

Antes de iniciar, é necessário ter instalado:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 📦 Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/Prog-LucasAlves/ENG_AirFlow-Faker-Docker.git
cd airflow-docker-postgres
```

2. Crie o arquivo .env com o conteúdo:

```env
# Airflow Core
AIRFLOW__CONNECTIONS__TEST_CONNECTIONS=True
AIRFLOW__CONNECTIONS__ALLOW_URI_AS_SECRET=true
AIRFLOW__CONNECTIONS__ALLOWED_PROTOCOLS=*
AIRFLOW__CORE__FERNET_KEY=''
AIRFLOW__CORE__EXECUTOR=LocalExecutor
AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=True
AIRFLOW__CORE__LOAD_EXAMPLES=False
AIRFLOW__CORE__TEST_CONNECTION=True
AIRFLOW_UID=0

# Backend DB
AIRFLOW__API__AUTH_BACKENDS=airflow.api.auth.backend.basic_auth
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
AIRFLOW__DATABASE__LOAD_DEFAULT_CONNECTIONS=0

# Airflow Init
_AIRFLOW_DB_MIGRATE=True
_AIRFLOW_WWW_USER_CREATE=True
_AIRFLOW_WWW_USER_USERNAME=airflow
_AIRFLOW_WWW_USER_PASSWORD=airflow
```

3. Suba os serviços:

```bash
docker compose up -d
```

4. Acesse a interface do Airflow:

```arduino
http://localhost:8080
```
