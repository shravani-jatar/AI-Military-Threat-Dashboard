import os
import joblib
from utils.data_loader import load_data
from utils.ml import train_severity_model

df = load_data()
model, metrics = train_severity_model(df)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/severity_model.joblib")

print(f"Model saved to models/severity_model.joblib")
print(f"Validation accuracy: {metrics['accuracy']:.4f}")
print(f"Weighted F1: {metrics['f1_weighted']:.4f}")
