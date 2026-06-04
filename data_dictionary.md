# Data Dictionary

## fact_nav

|Column|Type|Meaning|
|---|---|---|
|amfi_code|TEXT|Fund code|
|date|DATE|NAV date|
|nav|REAL|Net Asset Value|


## fact_transactions

|Column|Type|Meaning|
|---|---|---|
|investor_id|TEXT|Investor ID|
|transaction_type|TEXT|SIP/Lumpsum|
|amount_inr|REAL|Transaction amount|


## fact_performance

|Column|Type|Meaning|
|---|---|---|
|return_1yr_pct|REAL|1 year return|
|return_3yr_pct|REAL|3 year CAGR|
|sharpe_ratio|REAL|Risk adjusted return|