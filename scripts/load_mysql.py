import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# Project root
BASE = Path(__file__).resolve().parent.parent

engine = create_engine(
"mysql+pymysql://root:1234@localhost/bluestock_mf"
)

print("Connected")

# Read files

nav = pd.read_csv(
BASE / "data" / "processed" / "clean_nav_history.csv"
)

tx = pd.read_csv(
BASE / "data" / "processed" / "clean_investor_transactions.csv"
)

perf = pd.read_csv(
BASE / "data" / "processed" / "clean_scheme_performance.csv"
)

# Load tables

nav.to_sql(
"fact_nav",
engine,
if_exists="replace",
index=False
)

tx.to_sql(
"fact_transactions",
engine,
if_exists="replace",
index=False
)

perf.to_sql(
"fact_performance",
engine,
if_exists="replace",
index=False
)

print("All tables loaded")