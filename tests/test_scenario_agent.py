import pandas as pd
from agents.scenario import ScenarioAgent

def test_scenario_agent():
    df = pd.DataFrame({
        "FSA": ["A1A", "B2B"],
        "PREDICTED_RISK": [0.3, 0.5]
    })
    overrides = {"B2B": 0.9}
    agent = ScenarioAgent()
    result = agent.override(df, overrides)
    assert result[result["FSA"] == "B2B"]["PREDICTED_RISK"].iloc[0] == 0.9
