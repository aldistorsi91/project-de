def enrich_keywords(df, keywords):
    for word in keywords:
        col_name = f"Keyword_{word.capitalize()}"
        df[col_name] = df["Judul"].str.lower().str.contains(word)
    return df

def enrich_features(df):
    df["Judul_Length"] = df["Judul"].apply(len)
    df["Jumlah_Kata_Judul"] = df["Judul"].apply(lambda x: len(x.split()))
    df["Is_Series"] = df["Judul"].str.contains(r"#\d+", regex=True)
    df["Contains_Colon"] = df["Judul"].str.contains(":")
    return df
