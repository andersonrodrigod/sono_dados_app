import pandas as pd


def load_data(path="sleep.csv"):
    df = pd.read_csv(path)
    df = df.drop_duplicates()
    df["Sleep Disorder"] = df["Sleep Disorder"].fillna("Sem disturbio")

    return df


def mean_sleep_by_occupation(df):
    return df.groupby("Occupation")["Sleep Duration"].mean().reset_index()

def mean_stress_by_occupation(df):
    return df.groupby("Occupation")["Stress Level"].mean().reset_index()

def mean_daily_steps_by_occupation(df):
    return df.groupby("Occupation")["Daily Steps"].mean().reset_index()

def mean_quality_sleep_by_occupation(df):
    return df.groupby("Occupation")["Quality of Sleep"].mean().reset_index()