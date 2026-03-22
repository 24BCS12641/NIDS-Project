import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    "protocol": [6, 17, 6, 1, 6, 17, 1, 6],
    "length": [60, 1200, 500, 70, 1500, 2000, 100, 300],
    "label": [0, 1, 0, 0, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

X = df[["protocol", "length"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "nids_model.pkl")

print("Model trained and saved!")
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# Save results
joblib.dump({
    "model": model,
    "accuracy": accuracy,
    "confusion_matrix": cm.tolist()
}, "nids_model.pkl")
