import pandas as pd

class ScenarioAgent:
    def override(self, df: pd.DataFrame, overrides: dict) -> pd.DataFrame:
        df = df.copy()
        for fsa, new_risk in overrides.items():
            df.loc[df["FSA"] == fsa, "PREDICTED_RISK"] = new_risk
        return df
