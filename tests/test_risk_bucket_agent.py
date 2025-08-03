import pandas as pd
from agents.risk_bucket import RiskBucketAgent

def test_risk_bucket_agent():
    df = pd.DataFrame({"PREDICTED_RISK": [0.2, 0.4, 0.6, 0.8, 1.0]})
    agent = RiskBucketAgent(n_clusters=2)
    result = agent.assign_buckets(df)
    assert "RISK_BUCKET" in result.columns
    assert result["RISK_BUCKET"].nunique() == 2
