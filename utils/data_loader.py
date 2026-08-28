import os 
import zipfile 
import pandas as pd 
import streamlit as st 
 
DATA_PATH = "data/globalterrorismdb_0718dist.csv.zip" 
 
USECOLS = [ 
    "eventid", "iyear", "imonth", "iday", "country_txt", "region_txt", 
    "provstate", "city", "latitude", "longitude", "success", "suicide", 
    "multiple", "attacktype1_txt", "targtype1_txt", "weaptype1_txt", 
    "gname", "nkill", "nwound", "property", "summary" 
] 
 
@st.cache_data(show_spinner="Loading historical GTD data...") 
def load_data(path: str = DATA_PATH) -> pd.DataFrame: 
    if not os.path.exists(path): 
        raise FileNotFoundError( 
            f"Dataset not found at '{path}'. Copy " 
            "'globalterrorismdb_0718dist.csv.zip' into the data folder." 
        ) 
 
    with zipfile.ZipFile(path) as z: 
        csv_files = [n for n in z.namelist() if n.lower().endswith(".csv")] 
        if not csv_files: 
            raise ValueError("The dataset ZIP does not contain a CSV file.") 
        with z.open(csv_files[0]) as f: 
            df = pd.read_csv( 
                f, 
                usecols=lambda c: c in USECOLS, 
                encoding="latin1", 
                low_memory=False 
            ) 
 
    numeric_cols = [ 
        "iyear", "imonth", "iday", "latitude", "longitude", "success", 
        "suicide", "multiple", "nkill", "nwound", "property" 
    ] 
    for col in numeric_cols: 
        if col in df.columns: 
            df[col] = pd.to_numeric(df[col], errors="coerce") 
 
    for col in ["nkill", "nwound", "success", "suicide", "multiple", "property"]: 
        df[col] = df[col].fillna(0) 
 
    for col in [ 
        "country_txt", "region_txt", "provstate", "city", "attacktype1_txt", 
        "targtype1_txt", "weaptype1_txt", "gname" 
    ]: 
        df[col] = df[col].fillna("Unknown").astype(str) 
 
    df["casualties"] = df["nkill"] + df["nwound"] 
    df["year"] = df["iyear"].astype(int) 
 
    return df 
 
def data_ready() -> bool: 
    return os.path.exists(DATA_PATH) 
