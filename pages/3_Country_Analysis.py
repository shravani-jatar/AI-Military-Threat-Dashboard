import streamlit as st
import plotly.express as px
from utils.data_loader import load_data
from utils.analytics import attack_summary

st.title("🌎 Country Analysis")
df = load_data()

countries = sorted(df.country_txt.unique())
country = st.selectbox("Select country", countries, index=countries.index("India") if "India" in countries else 0)

work = df[df.country_txt == country].copy()
c1,c2,c3,c4 = st.columns(4)
c1.metric("Incidents", f"{len(work):,}")
c2.metric("Fatalities", f"{int(work.nkill.sum()):,}")
c3.metric("Injuries", f"{int(work.nwound.sum()):,}")
c4.metric("Success rate", f"{work.success.mean()*100:.1f}%")

annual = work.groupby("year", as_index=False).agg(
    incidents=("eventid","count"),
    fatalities=("nkill","sum"),
    injuries=("nwound","sum")
)
fig = px.line(annual, x="year", y="incidents", markers=True, title=f"{country}: Historical Incidents")
st.plotly_chart(fig, use_container_width=True)

a,b = st.columns(2)
with a:
    attack = attack_summary(work, "attacktype1_txt").head(10)
    fig2 = px.bar(attack.sort_values("incidents"), x="incidents", y="attacktype1_txt", orientation="h",
                  title="Top Attack Types")
    st.plotly_chart(fig2, use_container_width=True)
with b:
    target = attack_summary(work, "targtype1_txt").head(10)
    fig3 = px.bar(target.sort_values("incidents"), x="incidents", y="targtype1_txt", orientation="h",
                  title="Top Target Categories")
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("### Recent historical activity")
recent_start = max(int(work.year.max()) - 4, int(work.year.min()))
recent = work[work.year >= recent_start]
st.dataframe(
    recent[["year","country_txt","region_txt","city","attacktype1_txt","targtype1_txt","nkill","nwound","success"]]
    .sort_values(["year","nkill"], ascending=[False,False])
    .head(100),
    use_container_width=True,
    hide_index=True
)
