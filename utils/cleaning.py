def clean_price_column(df, column='Harga'):
    df[column] = df[column].astype(str).str.replace('£', '').astype(float)
    return df