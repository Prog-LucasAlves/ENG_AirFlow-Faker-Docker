FROM apache/airflow:latest-python3.12
USER root



USER airflow
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
