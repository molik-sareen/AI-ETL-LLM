import pandas as pd
import numpy as np

def clean_data(df):
    df.dropna(inplace=True)
    df = df[df["value"] > 0]  # Example condition
    return df

def feature_engineering(df):
    df["log_value"] = np.log1p(df["value"])
    return df

