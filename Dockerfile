FROM apache/airflow:3.0.4
USER airflow
RUN pip install --no-cache-dir polars pydantic requests pytest
COPY ./data /opt/airflow/data
