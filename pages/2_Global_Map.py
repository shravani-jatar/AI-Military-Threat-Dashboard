import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.title("🌍 Global Historical Threat Map")
df = load_data()

c1, c2 = st.columns(2)
with c1:
    start, end = st.slider(
        "Year range",
        int(df.year.min()), int(df.year.max()),
        (max(int(df.year.min()), 2000), int(df.year.max()))
    )
with c2:
    measure = st.selectbox("Map measure", ["Incidents", "Fatalities", "Injuries"])

work = df[(df.year >= start) & (df.year <= end)].copy()
metric = {"Incidents":"eventid", "Fatalities":"nkill", "Injuries":"nwound"}[measure]
agg = work.groupby("country_txt", as_index=False).agg(
    incidents=("eventid","count"),
    fatalities=("nkill","sum"),
    injuries=("nwound","sum")
)
agg["value"] = agg[metric].fillna(0) if metric != "eventid" else agg["incidents"]

fig = px.choropleth(
    agg, locations="country_txt", locationmode="country names",
    color="value", hover_name="country_txt",
    color_continuous_scale="Blues",
    title=f"{measure}: {start}–{end}"
)
fig.update_layout(height=650, margin=dict(l=0,r=0,t=55,b=0))
st.plotly_chart(fig, use_container_width=True)

st.caption("Map represents historical recorded activity only. It is not a real-time or predictive operational map.")
