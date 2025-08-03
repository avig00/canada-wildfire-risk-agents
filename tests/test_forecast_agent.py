import pandas as pd
from agents.forecast import ForecastAgent

def test_forecast_agent():
    df = pd.DataFrame({
        "FSA": ["A1A", "B2B", "C3C"],
        "YEAR": [2021, 2021, 2021],
        "AVG_NUM_FIRES": [2, 3, 1],
        "AVG_AREA_BURNT": [50, 70, 30],
        "DRY_DAYS": [10, 12, 8],
        "WIND_INDEX": [5, 7, 4],
        "TARGET": [0.3, 0.7, 0.2]
    })

    agent = ForecastAgent()
    agent.train(df)

    X_test = df.drop(columns=["FSA", "YEAR", "TARGET"])
    preds = agent.predict(X_test)

    assert len(preds) == 3
    assert preds.between(0, 1).all()
