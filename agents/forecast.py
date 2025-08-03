import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class ForecastAgent:
    def __init__(self):
        self.model = RandomForestRegressor(random_state=42)

    def train(self, df: pd.DataFrame):
        X = df.drop(columns=["FSA", "YEAR", "TARGET"])
        y = df["TARGET"]
        self.model.fit(X, y)

    def predict(self, X_new: pd.DataFrame) -> pd.Series:
        return pd.Series(self.model.predict(X_new), index=X_new.index, name="PREDICTED_RISK")
