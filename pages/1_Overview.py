import streamlit as st
import plotly.express as px
from utils.data_loader import load_data
from utils.analytics import yearly_summary

st.title("📊 Overview")
df = load_data()
annual = yearly_summary(df)

left, right = st.columns([2, 1])
with left:
    fig = px.line(
        annual, x="year", y="incidents",
        markers=True, title="Historical Incident Trend"
    )
    fig.update_layout(height=420, margin=dict(l=10,r=10,t=55,b=10))
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("#### Key observations")
    peak = annual.loc[annual["incidents"].idxmax()]
    st.metric("Peak incident year", int(peak["year"]))
    st.metric("Peak incidents", f"{int(peak['incidents']):,}")
    st.metric("Peak fatalities", f"{int(annual['fatalities'].max()):,}")

st.markdown("### Fatalities and injuries")
fig2 = px.area(
    annual, x="year", y=["fatalities", "injuries"],
    title="Recorded Human Impact Over Time"
)
fig2.update_layout(height=400)
st.plotly_chart(fig2, use_container_width=True)
