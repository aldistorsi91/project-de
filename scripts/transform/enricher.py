def enrich_keywords(df, keywords):
    for kw in keywords:
        col_name = f"Keyword_{kw.capitalize()}"
        df[col_name] = df["Judul"].str.lower().str.contains(kw)
    return df

def enrich_features(df):
    df["Judul_Length"] = df["Judul"].apply(len)
    df["Jumlah_Kata_Judul"] = df["Judul"].apply(lambda x: len(x.split()))
    df["Is_Series"] = df["Judul"].str.contains(r"#\d+", regex=True)
    df["Contains_Colon"] = df["Judul"].str.contains(":")
    return df
