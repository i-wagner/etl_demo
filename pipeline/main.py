from extract import extract_data
from transform import transform_data

URL = "~/Downloads/world-happiness/2015.csv"
if __name__ == "__main__":
    df = extract_data(URL)
    df = transform_data(df)
