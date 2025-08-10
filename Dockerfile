FROM apache/airflow:3.0.4

USER airflow

# Install Python dependencies
RUN pip install --no-cache-dir polars pydantic requests pytest

# Copy project files to container
COPY . /opt/airflow

# Set PYTHONPATH to include project directory (for module imports)
ENV PYTHONPATH=/opt/airflow:$PYTHONPATH