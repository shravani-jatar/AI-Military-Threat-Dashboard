import streamlit as st
from utils.data_loader import load_data

st.title("📊 Data Explorer")
df = load_data()

c1,c2,c3 = st.columns(3)
with c1:
    regions = st.multiselect("Region", sorted(df.region_txt.unique()))
with c2:
    attacks = st.multiselect("Attack type", sorted(df.attacktype1_txt.unique()))
with c3:
    year_range = st.slider(
        "Year range", int(df.year.min()), int(df.year.max()),
        (int(df.year.min()), int(df.year.max()))
    )

work = df[(df.year >= year_range[0]) & (df.year <= year_range[1])].copy()
if regions:
    work = work[work.region_txt.isin(regions)]
if attacks:
    work = work[work.attacktype1_txt.isin(attacks)]

st.write(f"Matching records: **{len(work):,}**")
display_cols = [
    "eventid","year","country_txt","region_txt","city",
    "attacktype1_txt","targtype1_txt","weaptype1_txt",
    "nkill","nwound","success","suicide"
]
st.dataframe(work[display_cols].head(5000), use_container_width=True, hide_index=True)

csv = work[display_cols].to_csv(index=False).encode("utf-8")
st.download_button(
    "Download filtered table (CSV)",
    data=csv,
    file_name="filtered_gtd_analysis.csv",
    mime="text/csv"
)
