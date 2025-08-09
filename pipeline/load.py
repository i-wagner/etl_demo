import sqlite3
import polars as pl


def load_data_to_sqlite(df: pl.DataFrame, db_path: str = "/opt/airflow/db/etl_demo.db"):
    try:
        conn = sqlite3.connect(db_path)
        df.write_database("world_happiness", conn, if_table_exists="replace")
        conn.close()
    except sqlite3.OperationalError as e:
        # TODO add logging
        print(f"Loading error: {e}")
