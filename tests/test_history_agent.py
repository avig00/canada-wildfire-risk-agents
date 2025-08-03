from agents.history import HistoryAgent

agent = HistoryAgent(
    fsa_path="data/raw/fsa/lfsa000b21a_e.shp",
    wildfire_path="data/raw/wildfire/NFDB_poly_20210707.shp"
)

df = agent.run()
print(df.head())
