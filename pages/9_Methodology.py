import streamlit as st

st.title("📚 Methodology & Limitations")

st.markdown("""
### Dataset
The project uses the supplied Global Terrorism Database (GTD) CSV. GTD is maintained by START at the University of Maryland and is intended for research and analysis of terrorism incidents.

### Preprocessing
- Read only the fields needed by the dashboard.
- Handle missing numeric values explicitly.
- Convert casualty fields to numeric values.
- Define `casualties = fatalities + injuries`.
- Keep categorical fields as strings with an `Unknown` category.

### AI severity model
The model is a Random Forest classifier trained on a sample of historical records.

Target:
- **Low:** 0 recorded casualties
- **Moderate:** 1–5 recorded casualties
- **High:** more than 5 recorded casualties

Features:
- year and month
- region
- attack type
- target category
- weapon category
- suicide indicator
- multiple incident indicator
- success indicator
- property-damage indicator

Performance shown in the dashboard is a held-out validation result and should not be presented as universal accuracy.

### Historical Exposure Index
The index combines:
- 35% historical incident frequency
- 30% average casualty severity
- 20% recent historical activity
- 15% historical success rate

The components are normalized to make the score interpretable.

### Forecasting
The forecasting module uses a simple linear regression over annual incident counts. It is intentionally presented as a trend projection rather than a reliable causal forecast.

### Limitations
- GTD is historical and does not represent live intelligence.
- Missing data and changes in data-collection methodology can affect trends.
- The 1993 GTD record set has known limitations.
- A machine-learning score is not a substitute for expert assessment.
- The dashboard should not be used for operational targeting, surveillance or real-world security decisions.

### Data source and citation
START (National Consortium for the Study of Terrorism and Responses to Terrorism), Global Terrorism Database, University of Maryland.

Official source:
https://www.start.umd.edu/gtd
""")
