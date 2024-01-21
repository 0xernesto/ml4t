def normalize_data(df):
    """Normalize asset prices using the first row of the dataframe."""
    return df / df.iloc[0, :]
