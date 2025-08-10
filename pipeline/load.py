import sqlite3
from sqlalchemy import create_engine
import polars as pl


# TODO switch to PostgreSQL
def load_data_to_sqlite(df: pl.DataFrame, db_path: str = "/opt/airflow/db/etl_demo.db"):
    try:
        engine = create_engine(f"sqlite:///{db_path}")
        df.write_database("world_happiness", engine, if_table_exists="replace")
        engine.dispose()
    except sqlite3.OperationalError as e:
        # TODO add logging
        print(f"Loading error: {e}")
