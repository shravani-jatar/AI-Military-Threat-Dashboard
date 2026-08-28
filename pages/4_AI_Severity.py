import streamlit as st
from utils.data_loader import load_data
from utils.ml import train_severity_model, predict_severity

st.title("🤖 AI Historical Severity Assessment")
st.write(
    "This module predicts a historical severity class from incident characteristics. "
    "It is not a model for predicting future attacks or operational targeting."
)

df = load_data()
model, metrics = train_severity_model(df)

st.success(
    f"Model validation — accuracy: {metrics['accuracy']*100:.1f}% | "
    f"weighted F1: {metrics['f1_weighted']*100:.1f}%"
)

c1,c2,c3 = st.columns(3)
with c1:
    year = st.number_input("Year", int(df.year.min()), int(df.year.max()), int(df.year.max()))
    month = st.slider("Month", 1, 12, 6)
    region = st.selectbox("Region", sorted(df.region_txt.unique()))
with c2:
    attack = st.selectbox("Attack type", sorted(df.attacktype1_txt.unique()))
    target = st.selectbox("Target category", sorted(df.targtype1_txt.unique()))
    weapon = st.selectbox("Weapon category", sorted(df.weaptype1_txt.unique()))
with c3:
    suicide = st.selectbox("Suicide indicator", [0,1])
    multiple = st.selectbox("Multiple incident indicator", [0,1])
    success = st.selectbox("Successful incident indicator", [0,1])
    property_damage = st.selectbox("Property damage indicator", [0,1])

row = {
    "iyear": year, "imonth": month, "region_txt": region,
    "attacktype1_txt": attack, "targtype1_txt": target,
    "weaptype1_txt": weapon, "suicide": suicide,
    "multiple": multiple, "success": success, "property": property_damage
}

if st.button("Run severity assessment", type="primary"):
    pred, probs = predict_severity(model, row)
    st.markdown(f"## Predicted historical severity: **{pred}**")
    st.dataframe(
        probs.assign(Probability=lambda x: (x["Probability"]*100).round(2)),
        use_container_width=True, hide_index=True
    )
