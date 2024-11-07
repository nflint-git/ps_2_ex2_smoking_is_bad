import polars as pl
from pathlib import Path

def read_data():
    path = Path(__file__).parent.parent / "data" / "smoking_data.csv"
    df = pl.read_csv(path) #for some reason the function was generating a new index, so used the original
    return df

def prep_data(df):
    df_cleaned = df.drop_nulls()
    df_renamed = df_cleaned.rename({
    "outcome": "alive",
    "smoker": "smokes"
    })
    df_transformed = df_renamed.with_columns(
        pl.when(pl.col("alive") == "Alive").then(1).otherwise(0).alias("alive")
    )
    return df_transformed