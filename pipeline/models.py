from pydantic import BaseModel, Field, field_validator


class HappinessRecord(BaseModel):
    country: str = Field(frozen=True)
    region: str = Field(frozen=True)
    happiness_rank: int = Field(ge=1, frozen=True)
    happiness_score: float = Field(ge=0, le=10, frozen=True)
    standard_error: float = Field(gt=0, frozen=True)
    economy_gdp_per_capita: float = Field(ge=0, frozen=True)
    family: float = Field(ge=0, frozen=True)
    health_life_expectancy: float = Field(ge=0, frozen=True)
    freedom: float = Field(ge=0, frozen=True)
    trust_government: float = Field(ge=0, frozen=True)
    generosity: float = Field(ge=0, frozen=True)
    dystopia_residual: float = Field(gt=0, frozen=True)

    @field_validator("country", "region")
    def non_empty(value: str) -> str:
        if not value.strip():
            raise ValueError("Field cannot be empty")
        return value
