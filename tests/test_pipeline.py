import pandas as pd
import pytest
from pipeline.models import HappinessRecord
from pipeline.transform import transform_data


def test_validation_success():
    HappinessRecord(
        Country="Germany",
        Region="Western Europe",
        Happiness_Rank=1,
        Happiness_Score=7.5,
        Economy_GDP_per_Capita=1.2,
    )


def test_transform_columns():
    df = pd.DataFrame(
        [
            {
                "Country": "Testland",
                "Region": "Europe",
                "Happiness Rank": 1,
                "Happiness Score": 7.5,
                "Economy (GDP per Capita)": 1.2,
            }
        ]
    )
    df = transform_data(df)
    assert "Happiness_Rank" in df.columns
