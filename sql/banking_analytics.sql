-- ============================================
-- BANKING DATA ANALYTICS
-- Amazon Redshift
-- ============================================

-- 1. Total Customers
SELECT COUNT(*) AS total_customers
FROM banking.customers;


-- 2. Total Accounts
SELECT COUNT(*) AS total_accounts
FROM banking.accounts;


-- 3. Total Deposits
SELECT SUM(balance) AS total_deposits
FROM banking.accounts;


-- 4. Average Account Balance
SELECT ROUND(AVG(balance), 2) AS average_balance
FROM banking.accounts;


-- 5. Total Transactions
SELECT COUNT(*) AS total_transactions
FROM banking.transactions;


-- 6. Active vs Inactive Customers
SELECT
    customer_status,
    COUNT(*) AS total_customers
FROM banking.customers
GROUP BY customer_status;


-- 7. Customers by State
SELECT
    state,
    COUNT(*) AS total_customers
FROM banking.customers
GROUP BY state
ORDER BY total_customers DESC;


-- 8. Customers by Occupation
SELECT
    occupation,
    COUNT(*) AS total_customers
FROM banking.customers
GROUP BY occupation
ORDER BY total_customers DESC;


-- 9. Customer Risk Distribution
SELECT
    risk_category,
    COUNT(*) AS total_customers
FROM banking.customers
GROUP BY risk_category;


-- 10. Deposits by Account Type
SELECT
    account_type,
    SUM(balance) AS total_deposits
FROM banking.accounts
GROUP BY account_type
ORDER BY total_deposits DESC;


-- 11. Average Balance by Account Type
SELECT
    account_type,
    ROUND(AVG(balance), 2) AS average_balance
FROM banking.accounts
GROUP BY account_type
ORDER BY average_balance DESC;


-- 12. Top 10 Customers by Account Balance
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    a.account_type,
    a.balance
FROM banking.customers c
JOIN banking.accounts a
    ON c.customer_id = a.customer_id
ORDER BY a.balance DESC
LIMIT 10;


-- 13. Transaction Type Distribution
SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM banking.transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;


-- 14. Payment Method Analysis
SELECT
    payment_method,
    COUNT(*) AS total_transactions
FROM banking.transactions
GROUP BY payment_method
ORDER BY total_transactions DESC;


-- 15. Transaction Status
SELECT
    status,
    COUNT(*) AS total_transactions
FROM banking.transactions
GROUP BY status;


-- 16. Loan Type Distribution
SELECT
    loan_type,
    COUNT(*) AS total_loans
FROM banking.loans
GROUP BY loan_type;


-- 17. Loan Portfolio by Type
SELECT
    loan_type,
    SUM(loan_amount) AS total_loan_amount
FROM banking.loans
GROUP BY loan_type
ORDER BY total_loan_amount DESC;


-- 18. Loan Status Distribution
SELECT
    loan_status,
    COUNT(*) AS total_loans
FROM banking.loans
GROUP BY loan_status;


-- 19. Card Type Distribution
SELECT
    card_type,
    COUNT(*) AS total_cards
FROM banking.cards
GROUP BY card_type;


-- 20. Card Network Distribution
SELECT
    card_network,
    COUNT(*) AS total_cards
FROM banking.cards
GROUP BY card_network;


-- 21. Branch-wise Total Deposits
SELECT
    b.branch_id,
    b.branch_name,
    COUNT(a.account_id) AS total_accounts,
    SUM(a.balance) AS total_deposits
FROM banking.branches b
JOIN banking.accounts a
    ON b.branch_id = a.branch_id
GROUP BY
    b.branch_id,
    b.branch_name
ORDER BY total_deposits DESC;


-- 22. Top 5 Branches by Deposits
SELECT
    b.branch_id,
    b.branch_name,
    COUNT(a.account_id) AS total_accounts,
    SUM(a.balance) AS total_deposits
FROM banking.branches b
JOIN banking.accounts a
    ON b.branch_id = a.branch_id
GROUP BY
    b.branch_id,
    b.branch_name
ORDER BY total_deposits DESC
LIMIT 5;


-- 23. Average Balance by Occupation
SELECT
    c.occupation,
    ROUND(AVG(a.balance), 2) AS average_balance
FROM banking.customers c
JOIN banking.accounts a
    ON c.customer_id = a.customer_id
GROUP BY c.occupation
ORDER BY average_balance DESC;


-- 24. State-wise Loan Portfolio
SELECT
    c.state,
    COUNT(l.loan_id) AS total_loans,
    SUM(l.loan_amount) AS total_loan_amount
FROM banking.customers c
JOIN banking.loans l
    ON c.customer_id = l.customer_id
GROUP BY c.state
ORDER BY total_loan_amount DESC;


-- 25. High-Income Customers with Low Balance
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.annual_income,
    a.account_id,
    a.balance
FROM banking.customers c
JOIN banking.accounts a
    ON c.customer_id = a.customer_id
WHERE c.annual_income > 1000000
  AND a.balance < 50000
ORDER BY c.annual_income DESC;


-- 26. Customers with More Than 10 Transactions
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(t.transaction_id) AS total_transactions
FROM banking.customers c
JOIN banking.accounts a
    ON c.customer_id = a.customer_id
JOIN banking.transactions t
    ON a.account_id = t.account_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
HAVING COUNT(t.transaction_id) > 10
ORDER BY total_transactions DESC;


-- 27. Customers Without Loans
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    a.account_id
FROM banking.customers c
JOIN banking.accounts a
    ON c.customer_id = a.customer_id
LEFT JOIN banking.loans l
    ON c.customer_id = l.customer_id
WHERE l.loan_id IS NULL;


-- 28. Top 3 Customers by Balance in Each Account Type
WITH ranked_customers AS
(
    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        a.account_type,
        a.balance,
        ROW_NUMBER() OVER
        (
            PARTITION BY a.account_type
            ORDER BY a.balance DESC
        ) AS rn
    FROM banking.customers c
    JOIN banking.accounts a
        ON c.customer_id = a.customer_id
)
SELECT
    customer_id,
    first_name,
    last_name,
    account_type,
    balance
FROM ranked_customers
WHERE rn <= 3
ORDER BY account_type, balance DESC;


-- 29. Customers Above Average Account Balance
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    a.balance
FROM banking.customers c
JOIN banking.accounts a
    ON c.customer_id = a.customer_id
WHERE a.balance >
(
    SELECT AVG(balance)
    FROM banking.accounts
)
ORDER BY a.balance DESC;


-- 30. Average Balance by Account Type using CTE
WITH average_bal AS
(
    SELECT
        account_type,
        AVG(balance) AS avg_bal
    FROM banking.accounts
    GROUP BY account_type
)
SELECT *
FROM average_bal
WHERE avg_bal > 500000
ORDER BY avg_bal DESC;


-- 31. Total Loan Amount by State using CTE
WITH loan_amt_state AS
(
    SELECT
        c.state,
        SUM(l.loan_amount) AS total_loan
    FROM banking.customers c
    JOIN banking.loans l
        ON c.customer_id = l.customer_id
    GROUP BY c.state
)
SELECT *
FROM loan_amt_state
WHERE total_loan > 50000000
ORDER BY total_loan DESC;