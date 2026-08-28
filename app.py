import streamlit as st
from pathlib import Path
from config.settings import APP_TITLE, APP_ICON, LAYOUT
from utils.data_loader import load_data, data_ready

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state="expanded"
)

css_path = Path("assets/styles.css")
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

st.sidebar.title("🛡️ Threat Analytics")
st.sidebar.caption("Historical AI-assisted intelligence dashboard")
st.sidebar.markdown("---")
st.sidebar.info("Dataset: Global Terrorism Database (historical)")
st.sidebar.warning("Academic analytics only — not an operational threat system.")

st.markdown("""
<div class="hero">
<h1>🛡️ AI-Based Military Intelligence & Threat Analytics</h1>
<p>Interactive historical analysis, explainable risk scoring, trend projection and machine-learning-based severity assessment.</p>
</div>
""", unsafe_allow_html=True)

if not data_ready():
    st.error("Dataset not found.")
    st.code("data/globalterrorismdb_0718dist.csv.zip")
    st.markdown(
        "Copy your supplied `globalterrorismdb_0718dist.csv.zip` into the project's `data` folder, then refresh the page."
    )
    st.stop()

try:
    df = load_data()
except Exception as exc:
    st.error("The dataset could not be loaded.")
    st.exception(exc)
    st.stop()

c1, c2, c3, c4 = st.columns(4)
metrics = [
    ("Total incidents", f"{len(df):,}", "Historical records"),
    ("Countries", f"{df['country_txt'].nunique():,}", "Countries represented"),
    ("Fatalities", f"{int(df['nkill'].sum()):,}", "Recorded fatalities"),
    ("Injuries", f"{int(df['nwound'].sum()):,}", "Recorded injuries"),
]
for col, (label, value, sub) in zip([c1,c2,c3,c4], metrics):
    with col:
        st.markdown(
            f'<div class="metric-card"><div class="metric-label">{label}</div>'
            f'<div class="metric-value">{value}</div><div class="metric-sub">{sub}</div></div>',
            unsafe_allow_html=True
        )

st.markdown("### What this project does")
a, b = st.columns(2)
with a:
    st.markdown("""
    **🌍 Historical Global Map**  
    Explore incident concentration by country.

    **🌎 Country Analysis**  
    Compare incidents, casualties, attack types and targets.

    **🤖 AI Severity Assessment**  
    Estimate historical severity class from incident characteristics.
    """)
with b:
    st.markdown("""
    **📈 Trend Projection**  
    Project historical incident-count trends.

    **🛡️ Historical Exposure Index**  
    An explainable index based on frequency, severity, recency and success rate.

    **🧠 Intelligence Brief**  
    Automatically summarize selected historical patterns.
    """)

st.markdown("### Dataset coverage")
st.write(
    f"The supplied dataset contains records from **{int(df['year'].min())} to {int(df['year'].max())}** "
    f"with {len(df):,} incidents."
)

st.caption(
    "Source: Global Terrorism Database (GTD), START / University of Maryland. "
    "Interpretations are statistical and historical, not operational."
)
