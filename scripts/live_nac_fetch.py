import requests
import pandas as pd

code=125497

url=f"https://api.mfapi.in/mf/{code}"

r=requests.get(url)

data=r.json()

df=pd.DataFrame(
data["data"]
)

df.to_csv(
"data/raw/live_nav.csv",
index=False
)

print("Done")