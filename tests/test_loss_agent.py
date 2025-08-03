import pandas as pd
from agents.loss import LossAgent

def test_loss_agent():
    df = pd.DataFrame({
        "PREDICTED_RISK": [0.3, 0.5],
        "EXPOSURE_INDEX": [100, 200]
    })
    agent = LossAgent()
    result = agent.estimate_losses(df)
    assert "EXPECTED_LOSS" in result.columns
    assert result["EXPECTED_LOSS"].tolist() == [30.0, 100.0]
