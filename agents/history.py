import geopandas as gpd
import pandas as pd
from pathlib import Path

class HistoryAgent:
    def __init__(self, fsa_path: str, wildfire_path: str, output_path: str = "data/processed/fsa_history_summary.csv"):
        self.fsa_path = Path(fsa_path)
        self.wildfire_path = Path(wildfire_path)
        self.output_path = Path(output_path)

    def run(self) -> pd.DataFrame:
        print("Loading FSA and wildfire shapefiles...")
        fsa = gpd.read_file(self.fsa_path).to_crs(epsg=4326)
        wildfire = gpd.read_file(self.wildfire_path).to_crs(epsg=4326)

        # Filter to recent fires (2000 onward)
        wildfire = wildfire[wildfire["YEAR"] >= 2000]
        wildfire = wildfire[["geometry", "YEAR", "SIZE_HA"]]

        print("Performing spatial join...")
        joined = gpd.sjoin(
            wildfire,
            fsa[["CFSAUID", "PRUID", "PRNAME", "LANDAREA", "geometry"]],
            how="inner",
            predicate="intersects"
        )

        print("Aggregating wildfire history features per FSA...")
        summary = joined.groupby("CFSAUID").agg(
            PRUID=("PRUID", "first"),
            PRNAME=("PRNAME", "first"),
            LANDAREA=("LANDAREA", "first"),
            num_wildfires=("YEAR", "count"),
            total_area_burned=("SIZE_HA", "sum"),
            avg_area_burned=("SIZE_HA", "mean"),
            years_with_fires=("YEAR", lambda x: x.nunique())
        ).reset_index()

        summary["fires_per_100km2"] = summary["num_wildfires"] / (summary["LANDAREA"] / 100)
        summary["burned_percent"] = (summary["total_area_burned"] / summary["LANDAREA"]) * 100

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        summary.to_csv(self.output_path, index=False)
        print(f"Saved FSA wildfire history to: {self.output_path}")

        return summary
