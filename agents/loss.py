import pandas as pd

class LossAgent:
    def estimate_losses(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["EXPECTED_LOSS"] = df["PREDICTED_RISK"] * df["EXPOSURE_INDEX"]
        return df
