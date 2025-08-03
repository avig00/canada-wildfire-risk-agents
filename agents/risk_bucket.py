import pandas as pd
from sklearn.cluster import KMeans

class RiskBucketAgent:
    def __init__(self, n_clusters=3):
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)

    def assign_buckets(self, df: pd.DataFrame, column: str = "PREDICTED_RISK") -> pd.DataFrame:
        df = df.copy()
        df["RISK_BUCKET"] = self.kmeans.fit_predict(df[[column]])
        return df
