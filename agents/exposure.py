import pandas as pd

class ExposureAgent:
    def calculate_exposure_index(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["EXPOSURE_INDEX"] = 1.0
        return df