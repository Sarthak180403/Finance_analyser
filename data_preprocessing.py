# ==========================================
# Data Processing Module
# ==========================================

import pandas as pd


def load_data(uploaded_file):
    """
    Reads the uploaded CSV file and performs basic preprocessing.
    """

    # Read CSV file
    df = pd.read_csv(uploaded_file)

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Convert Date column into datetime format
    df["Date"] = pd.to_datetime(
        df["Date"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    return df