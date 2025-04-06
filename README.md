
# 🌀 Projeto Airflow + Docker + PostgreSQL

Este projeto tem como objetivo demonstrar uma arquitetura simples e funcional para orquestração de pipelines utilizando **Apache Airflow** em conjunto com **Docker** e **PostgreSQL**. A stack é ideal para fluxos de dados programáveis, com controle total sobre agendamentos, logs e estados de execução.

**Banco de dados utlizado do Projeto [AED_DBT](...)

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
├── dags/                 # Arquivos com os fluxos de trabalho (DAGs)
│   └── example_dag.py
├── .env                  # Variáveis de ambiente
├── Dockerfile            # Imagem customizada do Airflow
├── docker-compose.yml    # Orquestração dos serviços

```
