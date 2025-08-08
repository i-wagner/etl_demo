import polars as pl


def extract_data(url):
    return pl.read_csv(url)
