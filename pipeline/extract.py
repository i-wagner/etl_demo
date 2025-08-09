import polars as pl

from models import HappinessRecord


# TODO add extraction of a JSON from some API endpoint
def extract_data(url):
    return pl.read_csv(url)


def validate_data(df: pl.DataFrame):
    valid_rows = []
    for row in df.iter_rows(named=True):
        try:
            record = HappinessRecord(
                country=row["Country"],
                region=row["Region"],
                happiness_rank=row["Happiness Rank"],
                happiness_score=row["Happiness Score"],
                standard_error=row["Standard Error"],
                economy_gdp_per_capita=row["Economy (GDP per Capita)"],
                family=row["Family"],
                health_life_expectancy=row["Health (Life Expectancy)"],
                freedom=row["Freedom"],
                trust_government=row["Trust (Government Corruption)"],
                generosity=row["Generosity"],
                dystopia_residual=row["Dystopia Residual"],
            )
            valid_rows.append(record)
        except Exception as e:
            # TODO add logging
            print(f"Validation error: {e}")
    return pl.DataFrame(valid_rows)
