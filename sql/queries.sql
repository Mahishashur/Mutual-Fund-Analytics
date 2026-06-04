-- 1 Average NAV
SELECT AVG(nav)
FROM fact_nav;


-- 2 Transaction Count
SELECT transaction_type, COUNT(*) FROM fact_transactions
GROUP BY transaction_type;


-- 3 Top Returns
SELECT * FROM fact_performance ORDER BY return_3yr_pct DESC
LIMIT 5;


-- 4 Expense Ratio <1
SELECT * FROM fact_performance WHERE expense_ratio_pct < 1;


-- 5 Avg Transaction
SELECT AVG(amount_inr) FROM fact_transactions;


-- 6 Count KYC
SELECT kyc_status, COUNT(*) FROM fact_transactions
GROUP BY kyc_status;


-- 7 Max NAV
SELECT MAX(nav) FROM fact_nav;


-- 8 Min NAV
SELECT MIN(nav) FROM fact_nav;


-- 9 Total Transactions
SELECT COUNT(*) FROM fact_transactions;


-- 10 Top Sharpe

SELECT * FROM fact_performance 
ORDER BY sharpe_ratio DESC LIMIT 5;