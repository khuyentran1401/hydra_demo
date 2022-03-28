import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(data_name: str) -> pd.DataFrame:
    return pd.read_csv(data_name)


def drop_na(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()


def get_age(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(age=df["Year_Birth"].apply(lambda row: 2021 - row))


def get_total_children(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(total_children=df["Kidhome"] + df["Teenhome"])


def get_total_purchases(df: pd.DataFrame) -> pd.DataFrame:
    purchases_columns = df.filter(like="Purchases", axis=1).columns
    return df.assign(total_purchases=df[purchases_columns].sum(axis=1))


def get_enrollment_years(df: pd.DataFrame) -> pd.DataFrame:
    df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], format="%d-%m-%Y")
    return df.assign(enrollment_years=2022 - df["Dt_Customer"].dt.year)


def get_family_size(df: pd.DataFrame, size_map: dict) -> pd.DataFrame:
    return df.assign(family_size=df["Marital_Status"].map(size_map) + df["total_children"])


def drop_features(df: pd.DataFrame, keep_columns: list):
    df = df[keep_columns]
    return df


def drop_outliers(df: pd.DataFrame, column_threshold: dict):
    for col, threshold in column_threshold.items():
        df = df[df[col] < threshold]
    return df.reset_index(drop=True)


def drop_columns_and_rows(df: pd.DataFrame, keep_columns: list, remove_outliers_threshold: dict):
    return df.pipe(drop_features, keep_columns=keep_columns).pipe(
        drop_outliers, column_threshold=remove_outliers_threshold
    )


def scale_features(df: pd.DataFrame):
    scaler = StandardScaler()
    return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)


def process_data():

    family_size = {
        "Married": 2,
        "Together": 2,
        "Absurd": 1,
        "Widow": 1,
        "YOLO": 1,
        "Divorced": 1,
        "Single": 1,
        "Alone": 1,
    }

    keep_columns = [
        "Income",
        "Recency",
        "NumWebVisitsMonth",
        "AcceptedCmp3",
        "AcceptedCmp4",
        "AcceptedCmp5",
        "AcceptedCmp1",
        "AcceptedCmp2",
        "Complain",
        "Response",
        "age",
        "total_purchases",
        "enrollment_years",
        "family_size",
    ]

    remove_outliers_threshold = {
        "age": 90,
        "Income": 600000,
    }

    df = load_data("data/raw/marketing_campaign.csv")
    df = drop_na(df)
    df = get_age(df)
    df = get_total_children(df)
    df = get_total_purchases(df)
    df = get_enrollment_years(df)
    df = get_family_size(df, family_size)
    df = drop_columns_and_rows(df, keep_columns, remove_outliers_threshold)
    df = scale_features(df)
    df.to_csv("data/intermediate/processed.csv", index=False)


if __name__ == "__main__":
    process_data()
