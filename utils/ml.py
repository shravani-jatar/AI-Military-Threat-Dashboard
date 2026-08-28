import numpy as np
import pandas as pd
import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

FEATURES = [
    "iyear", "imonth", "region_txt", "attacktype1_txt",
    "targtype1_txt", "weaptype1_txt", "suicide", "multiple",
    "success", "property"
]

CATEGORICAL = [
    "region_txt", "attacktype1_txt", "targtype1_txt", "weaptype1_txt"
]

@st.cache_resource(show_spinner="Training the historical severity model...")
def train_severity_model(df):
    work = df[FEATURES + ["nkill", "nwound"]].copy()
    work["casualties"] = work["nkill"].fillna(0) + work["nwound"].fillna(0)
    work["severity"] = pd.cut(
        work["casualties"],
        bins=[-1, 0, 5, np.inf],
        labels=["Low", "Moderate", "High"]
    ).astype(str)

    sample_n = min(80000, len(work))
    work = work.sample(sample_n, random_state=42)

    X = work[FEATURES].copy()
    y = work["severity"]

    for col in CATEGORICAL:
        X[col] = X[col].fillna("Unknown").astype(str)

    numeric = [c for c in FEATURES if c not in CATEGORICAL]

    pre = ColumnTransformer(
        [("cat", OneHotEncoder(
            handle_unknown="ignore",
            min_frequency=3
        ), CATEGORICAL)],
        remainder="passthrough"
    )

    pipe = Pipeline([
        ("preprocess", pre),
        ("model", RandomForestClassifier(
            n_estimators=80,
            max_depth=16,
            min_samples_leaf=3,
            class_weight="balanced_subsample",
            n_jobs=-1,
            random_state=42
        ))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )
    pipe.fit(X_train, y_train)
    pred = pipe.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, pred),
        "f1_weighted": f1_score(y_test, pred, average="weighted")
    }
    return pipe, metrics

def predict_severity(model, row):
    X = pd.DataFrame([row])
    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]
    classes = model.classes_
    probs = pd.DataFrame({"Severity": classes, "Probability": probabilities})
    return prediction, probs
