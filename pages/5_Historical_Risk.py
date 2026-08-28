import streamlit as st
import plotly.express as px
from utils.data_loader import load_data
from utils.analytics import historical_exposure_index

st.title("🛡️ Historical Exposure Index")
st.write(
    "An explainable index for comparing historical patterns in the dataset. "
    "It is not a live threat score."
)
df = load_data()
table = historical_exposure_index(df)

topn = st.slider("Countries to display", 5, 30, 15)
show = table.head(topn).copy()

fig = px.bar(
    show.sort_values("exposure_index"),
    x="exposure_index", y="country_txt", orientation="h",
    color="exposure_level",
    title="Highest Historical Exposure Index"
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Components")
st.dataframe(
    show[[
        "country_txt","exposure_index","exposure_level","incidents",
        "fatalities","avg_casualties","recent_activity","success_rate"
    ]].rename(columns={
        "country_txt":"Country",
        "exposure_index":"Index",
        "exposure_level":"Level",
        "incidents":"Incidents",
        "fatalities":"Fatalities",
        "avg_casualties":"Avg casualties/incident",
        "recent_activity":"Recent activity",
        "success_rate":"Success rate %"
    }).round(2),
    use_container_width=True, hide_index=True
)

st.info(
    "Formula: 35% historical frequency + 30% average casualty severity + "
    "20% recent activity + 15% historical success rate."
)
