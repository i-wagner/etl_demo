# Demo for a Python-based ETL pipeline

This repository contains a lightweight demo, showcasing how to implement a Python-based ETL pipeline.

Data is extracted from a local `.csv` file, validated, transformed and loaded into a local SQLite database. The pipeline is orchestrated and scheduled as a Airflow DAG. Airflow itself is containerized within a Docker container.

Note: `docker-compose.yml` contains a minimal configuration with all mandatory components to run Airflow. It is based on the [official sample file](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#fetching-docker-compose-yaml), provided by Airflow, and is not optimized for production environments.

---

## Setup

1. Clone this repository

```
git clone https://github.com/i-wagner/etl_demo.git
```

2. Install [```uv```](https://github.com/astral-sh/uv) (if you haven’t yet)

With the standalone installer:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

With pip:
```
pip install uv
```

3. Start the Docker container

```
cd etl_demo
docker compose up
```

The Airflow GUI can be accessed via http://localhost:8080/, using `airflow` `airflow` as login credentials. The DAG can then be run directly from within Airflow.

4. Shutdown Docker container

When done, run `docker compose down`

(5. Local runs)

The pipeline can be run locally, without the need to spin up the Docker container, using `PYTHONPATH=. uv run ./pipeline/main.py`
`PYTHONPATH=.` needs to run to add the entire folder to the Python path, otherwise the pipeline module won't be found.

---

## Repository structure

The repository structure and key scripts are highlighted below:

```
etl_demo/
├─ pyproject.toml # Project configuration
├─ uv.lock # Lockfile with exact information about project dependencies
├───config/ # Airflow config file
├───dags/ # Folder with DAGs
├───data/
│    ├─ world-happiness/
     Sample data to extract, load, and transform
├───pipeline/
│    Scripts to run all steps of the pipeline
│    ├─ extract.py
│    ├─ load.py
│    ├─ transform.py
│    ├─ models.py # Schema definition for source data
│    ├─ main.py  # Entrypoint
```

