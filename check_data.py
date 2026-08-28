from utils.data_loader import load_data

df = load_data()
print("Dataset loaded successfully.")
print("Rows:", len(df))
print("Columns used:", len(df.columns))
print("Year range:", int(df.year.min()), "-", int(df.year.max()))
print("Countries:", df.country_txt.nunique())
print("Fatalities:", int(df.nkill.sum()))
print("Injuries:", int(df.nwound.sum()))
