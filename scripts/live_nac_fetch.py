import requests
import pandas as pd

scheme_code = 125497

api_endpoint = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(api_endpoint)

response_content = response.json()

mutual_fund_data = pd.DataFrame(
    response_content["data"]
)

mutual_fund_data.to_csv(
    "data/raw/live_nav.csv",
    index=False
)

print("Ok")