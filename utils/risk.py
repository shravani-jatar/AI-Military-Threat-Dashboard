from .analytics import historical_exposure_index

def get_country_exposure(df, country):
    table = historical_exposure_index(df)
    row = table[table["country_txt"] == country]
    if row.empty:
        return None
    return row.iloc[0].to_dict()
