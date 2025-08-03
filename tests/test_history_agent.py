import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon, Point
from unittest.mock import patch, MagicMock
from agents.history import HistoryAgent

def mock_fsa_data():
    return gpd.GeoDataFrame({
        'CFSAUID': ['A1A'],
        'PRUID': [10],
        'PRNAME': ['Alberta'],
        'LANDAREA': [1000],
        'geometry': [Polygon([(0, 0), (0, 5), (5, 5), (5, 0)])]
    }, crs="EPSG:4326")

def mock_wildfire_data():
    return gpd.GeoDataFrame({
        'YEAR': [2005, 2010],
        'SIZE_HA': [50, 100],
        'geometry': [Point(1, 1), Point(2, 2)]
    }, crs="EPSG:4326")

@patch("geopandas.read_file")
def test_history_agent(mock_read_file, tmp_path):
    # Patch GeoPandas read_file to return mock data
    mock_read_file.side_effect = [mock_fsa_data(), mock_wildfire_data()]

    output_csv = tmp_path / "summary.csv"
    agent = HistoryAgent("fake_fsa.shp", "fake_fire.shp", output_csv)
    result = agent.run()

    expected_columns = {
        'CFSAUID', 'PRUID', 'PRNAME', 'LANDAREA',
        'num_wildfires', 'total_area_burned', 'avg_area_burned',
        'years_with_fires', 'fires_per_100km2', 'burned_percent'
    }

    assert isinstance(result, pd.DataFrame)
    assert expected_columns.issubset(set(result.columns))
    assert output_csv.exists()

