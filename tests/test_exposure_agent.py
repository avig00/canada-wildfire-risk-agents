import pandas as pd
from agents.exposure import ExposureAgent

def test_exposure_agent():
    df = pd.DataFrame({"FSA": ["A1A", "B2B"]})
    agent = ExposureAgent()
    result = agent.calculate_exposure_index(df)
    assert "EXPOSURE_INDEX" in result.columns
    assert (result["EXPOSURE_INDEX"] == 1.0).all()
