def fill_missing(df_data):
    """Fill missing values in data frame, in place."""
    df_data.ffill(inplace=True)
    df_data.bfill(inplace=True)
