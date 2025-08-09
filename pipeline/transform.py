import polars as pl
import re


def transform_data(df: pl.DataFrame) -> pl.DataFrame:
    df.columns = [
        (re.sub(r"[()]", "", col).lower().replace(" ", "_")) for col in df.columns
    ]
    return df
