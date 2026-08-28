import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_incidents(df, entity=None, horizon=5):
    if entity and entity != "Global":
        data = df[df["country_txt"] == entity]
    else:
        data = df

    annual = data.groupby("year").size().reset_index(name="incidents")
    if len(annual) < 5:
        raise ValueError("At least five historical years are required for a trend projection.")

    model = LinearRegression()
    model.fit(annual[["year"]], annual["incidents"])

    future_years = np.arange(
        int(annual["year"].max()) + 1,
        int(annual["year"].max()) + horizon + 1
    )
    pred = np.maximum(
        0,
        model.predict(pd.DataFrame({"year": future_years}))
    )

    forecast = pd.DataFrame({
        "year": future_years,
        "incidents": pred.round().astype(int),
        "type": "Trend projection"
    })
    historical = annual.assign(type="Historical")
    combined = pd.concat([historical, forecast], ignore_index=True)

    return combined, model
