from extract import extract_data, validate_data
from transform import transform_data
from load import load_data_to_sqlite


def run_pipeline():
    df = extract_data(URL)
    df = validate_data(df)
    df = transform_data(df)
    load_data_to_sqlite(df)


URL = "~/Downloads/world-happiness/2015.csv"
if __name__ == "__main__":
    run_pipeline()
