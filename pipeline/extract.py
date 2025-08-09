import polars as pl

# TODO add extraction of a JSON from some API endpoint
def extract_data(url):
    return pl.read_csv(url)
