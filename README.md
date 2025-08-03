# 🇨🇦 Canada Wildfire Risk Simulation (Agent-Based)

A modular wildfire risk, exposure, and suppression simulation system using public Canadian data.

## Agents
- `HistoryAgent`: Computes FSA-level wildfire metrics from 2000+
- `ForecastAgent`: Predicts short-term wildfire risk from weather + history
- `ExposureAgent`: Estimates human/economic exposure
- `LossAgent`: Combines risk + exposure into dollar losses
- `ScenarioAgent`: Simulates "what-if" conditions
- `SuppressionAgent`: Models firefighting resource gaps using (s, S)

## Setup

```bash
conda env create -f environment.yml
conda activate can_wildfire_agents
```

## Data

FSAs: Statistique Canada
Wildfire features: National Fire Database