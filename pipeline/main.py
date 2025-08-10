from pipeline.extract import extract_data, validate_data
from pipeline.transform import transform_data
from pipeline.load import load_data_to_sqlite


def run_pipeline(url: str):
    df = extract_data(url)
    df = validate_data(df)
    df = transform_data(df)
    load_data_to_sqlite(df)


URL = "/opt/airflow/data/world-happiness/2015.csv"
if __name__ == "__main__":
    run_pipeline(url=URL)
