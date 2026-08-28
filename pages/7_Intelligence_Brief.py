import streamlit as st
from utils.data_loader import load_data
from utils.analytics import attack_summary

st.title("🧠 Automated Intelligence Brief")
df = load_data()

countries = ["Global"] + sorted(df.country_txt.unique())
country = st.selectbox("Scope", countries)
years = st.slider(
    "Historical period",
    int(df.year.min()), int(df.year.max()),
    (max(int(df.year.min()), 2010), int(df.year.max()))
)

work = df[(df.year >= years[0]) & (df.year <= years[1])].copy()
if country != "Global":
    work = work[work.country_txt == country]

if work.empty:
    st.warning("No records match the selected filters.")
    st.stop()

top_attack = attack_summary(work, "attacktype1_txt").iloc[0]
top_target = attack_summary(work, "targtype1_txt").iloc[0]
top_region = work["region_txt"].value_counts().index[0]

st.markdown("### Executive summary")
st.write(
    f"Between **{years[0]} and {years[1]}**, the selected scope contains "
    f"**{len(work):,} recorded incidents**, with **{int(work.nkill.sum()):,} fatalities** "
    f"and **{int(work.nwound.sum()):,} injuries**."
)

c1,c2,c3 = st.columns(3)
c1.metric("Most common attack type", top_attack["attacktype1_txt"])
c2.metric("Most common target category", top_target["targtype1_txt"])
c3.metric("Most represented region", top_region)

st.markdown("### Analytical observations")
st.markdown(f"""
- The dominant recorded attack type is **{top_attack['attacktype1_txt']}**.
- The most frequent target category is **{top_target['targtype1_txt']}**.
- The average recorded casualties per incident are **{work['casualties'].mean():.2f}**.
- The historical success rate in the selected records is **{work['success'].mean()*100:.1f}%**.
- These observations describe the selected historical sample; they do not establish causation or predict future events.
""")
