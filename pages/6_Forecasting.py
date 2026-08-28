import streamlit as st
import plotly.express as px
from utils.data_loader import load_data
from utils.forecast import forecast_incidents

st.title("📈 Trend Forecasting")
df = load_data()

entity = st.selectbox(
    "Forecast scope",
    ["Global"] + sorted(df.country_txt.unique())
)
horizon = st.slider("Projection horizon (years)", 1, 5, 3)

try:
    combined, model = forecast_incidents(df, entity, horizon)
    fig = px.line(
        combined, x="year", y="incidents", color="type",
        markers=True, title=f"{entity}: Historical Trend + Linear Projection"
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        combined.tail(horizon)[["year","incidents","type"]],
        use_container_width=True, hide_index=True
    )

    st.warning(
        "This is a simple statistical trend projection. It does not account for "
        "political, economic, reporting, policy or conflict changes and should not "
        "be interpreted as a real-world forecast."
    )
except ValueError as exc:
    st.error(str(exc))
