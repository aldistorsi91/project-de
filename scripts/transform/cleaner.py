def clean_prices(df):
    df["Harga"] = (
        df["Harga"]
        .astype(str)
        .str.replace("Â£", "")
        .str.replace("£", "")
        .str.replace("Â", "")
        .str.replace("�", "")
        .astype(float)
    )
    return df