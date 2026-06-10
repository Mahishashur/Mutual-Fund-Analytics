import pandas as pd

perf=pd.read_csv(
    "data/processed/clean_scheme_performance.csv")

risk=input("Risk (Low Moderate High): ")

out=(perf.sort_values("sharpe_ratio",ascending=False).head(3))

print(out)


hhi=(
portfolio.groupby(["amfi_code","sector"])
["weight_pct"].sum())

hhi=(hhi**2).groupby(level=0).sum()
hhi.head()