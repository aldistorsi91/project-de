def add_keyword_flags(df, keyword_dict):
    for col, kw in keyword_dict.items():
        df[col] = df['Judul'].str.lower().str.contains(kw)
    return df