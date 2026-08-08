🏦 Banking Data Engineering & Analytics

An end-to-end banking data engineering and analytics project built using Python, Amazon S3, AWS Glue, AWS Glue Data Catalog, Amazon Redshift Serverless, SQL, and Microsoft Power BI.

📌 Project Overview

This project demonstrates a complete cloud data workflow:

Python/Faker → Amazon S3 → AWS Glue ETL → Parquet → Glue Data Catalog → Amazon Redshift → SQL Analytics → Power BI

The project covers six banking entities:

Customers

Accounts

Transactions

Branches

Loans

Cards

The objective is to transform synthetic banking data into a structured analytical warehouse and build business-focused Power BI insights.

🏗️ Architecture

Synthetic Banking Data
        │
        ▼
   Python + Faker
        │
        ▼
   Amazon S3
    Raw Data
        │
        ▼
    AWS Glue
     ETL Job
        │
        ├── Transform data
        ├── Standardize data types
        └── Convert to Parquet
        │
        ▼
   Amazon S3
Processed Parquet Data
        │
        ▼
 AWS Glue Crawlers
        │
        ▼
AWS Glue Data Catalog
        │
        ▼
Amazon Redshift
    Serverless
        │
        ▼
   SQL Analytics
        │
        ▼
    Power BI
   Dashboard

🛠️ Technologies Used

Category

Technology

Programming

Python

Data Generation

Faker, Pandas

Cloud Storage

Amazon S3

ETL

AWS Glue

Metadata

AWS Glue Data Catalog

Crawling

AWS Glue Crawlers

File Format

Apache Parquet

Data Warehouse

Amazon Redshift Serverless

Analytics

SQL

Visualization

Microsoft Power BI

Calculations

DAX

Version Control

Git / GitHub

📂 Dataset

The project uses synthetically generated banking data for educational and portfolio purposes.

Table

Description

customers

Customer demographic, income, KYC, status, and risk information

accounts

Bank account, balance, type, status, and branch information

transactions

Transaction date, amount, type, merchant, payment method, and status

branches

Branch location, code, manager, region, and contact information

loans

Loan type, amount, interest rate, tenure, EMI, dates, and status

cards

Card type, network, issue/expiry dates, limits, and status

Customer Columns

customer_id, first_name, last_name, gender, dob, phone, email,
address, city, state, pincode, occupation, annual_income,
marital_status, customer_since, kyc_status, customer_status,
risk_category

Account Columns

account_id, customer_id, account_type, balance,
opening_date, account_status, branch_id

Transaction Columns

transaction_id, account_id, transaction_date, transaction_type,
amount, merchant, payment_method, city, status, remarks

Branch Columns

branch_id, branch_name, branch_code, ifsc_code, city, state,
region, address, manager_name, phone, email, opened_date

Loan Columns

loan_id, customer_id, loan_type, loan_amount, interest_rate,
loan_term_months, emi, start_date, end_date, loan_status

Card Columns

card_id, customer_id, account_id, card_number, card_type,
card_network, issue_date, expiry_date, cvv, daily_limit, status

Data privacy: The data is synthetic. Raw files containing personal-looking fields such as phone numbers, email addresses, addresses, card numbers, or CVVs should not be uploaded to this public repository.

🔄 ETL Pipeline

1. Synthetic Data Generation

Python and Faker were used to generate realistic-looking synthetic banking records for customers, accounts, transactions, branches, loans, and cards.

2. Amazon S3 — Raw Layer

Raw datasets were uploaded to Amazon S3.

raw/
├── customers/
├── accounts/
├── transactions/
├── branches/
├── loans/
└── cards/

3. AWS Glue ETL

A single AWS Glue ETL job was used to process the six banking datasets.

The pipeline:

Reads raw data from S3.

Processes each banking entity.

Applies required transformations.

Standardizes data types.

Handles date fields.

Converts the processed datasets to Parquet.

Writes the results to S3.

Processed structure:

processed/
├── customers/
├── accounts/
├── transactions/
├── branches/
├── loans/
└── cards/

4. AWS Glue Crawlers

Glue Crawlers were used to discover the schemas of the processed Parquet datasets and populate the AWS Glue Data Catalog.

5. Amazon Redshift Serverless

The processed datasets were loaded into Amazon Redshift Serverless.

Schema:

banking

Tables:

customers
accounts
transactions
branches
loans
cards

🗃️ Data Model

The main logical relationships are:

customers
   │
   ├── accounts
   ├── loans
   └── cards

branches
   │
   └── accounts

Data Quality Finding

During Power BI relationship validation, four account_id values were found more than once:

ACC14191973
ACC15485194
ACC50932665
ACC56678647

These were not exact duplicate rows. The repeated account IDs were associated with different customer/account attributes.

Because a reliable unique key was not available for those records, an accounts → transactions one-to-many relationship was not forced in Power BI. This avoids potentially incorrect filtering and financial aggregations.

This demonstrates the importance of validating key uniqueness before building analytical relationships.

📊 SQL Analytics

SQL was used in Amazon Redshift to answer business questions across customers, accounts, transactions, branches, loans, and cards.

Customer Analytics

Total customers

Customers by state

Customers by occupation

Active vs inactive customers

Customer risk distribution

KYC status

High-income customers with low balances

Customers above average account balance

Account Analytics

Total accounts

Total deposits

Average account balance

Deposits by account type

Top customers by balance

Branch-wise deposits

Average balance by account type

Transaction Analytics

Total transactions

Transaction type distribution

Payment method analysis

Transaction status analysis

Customers with more than a specified number of transactions

Loan Analytics

Total loan portfolio

Loan portfolio by loan type

Loan status distribution

State-wise loan portfolio

EMI analysis

Card Analytics

Card type distribution

Card network distribution

Card status analysis

🧠 SQL Concepts Demonstrated

SELECT
WHERE
ORDER BY
GROUP BY
HAVING
COUNT()
SUM()
AVG()
INNER JOIN
LEFT JOIN
Subqueries
CTEs
ROW_NUMBER()
PARTITION BY

The SQL analytics file is available at:

sql/banking_analytics.sql

📈 Power BI Dashboard

Amazon Redshift was connected directly to Microsoft Power BI.

The Power BI model contains DAX measures and business-focused visuals.

KPI Cards

Total Customers

Total Accounts

Total Deposits

Total Loans

Total Transactions

Average Account Balance

Dashboard Visualizations

Customers by State

Deposits by Account Type

Loan Amount by Loan Type

Transaction Type Distribution

Top 10 Branches by Deposits

Customer Risk Distribution

📐 DAX Measures

Total Customers =
COUNT(customers[customer_id])

Total Accounts =
COUNT(accounts[account_id])

Total Deposits =
SUM(accounts[balance])

Total Loans =
SUM(loans[loan_amount])

Total Transactions =
COUNT(transactions[transaction_id])

Average Balance =
AVERAGE(accounts[balance])

🔍 Business Questions Answered

How many customers does the bank have?

How many accounts are maintained?

What is the total deposit balance?

Which account types contribute the most deposits?

Which branches have the highest deposits?

Which states have the largest customer base?

What is the total loan portfolio?

Which loan types contribute the most to the loan portfolio?

How are customers distributed across risk categories?

What transaction types are most common?

Which customers have the highest account balances?

What patterns can be identified across customer and financial data?

📁 Repository Structure

banking-data-engineering-analytics/
│
├── README.md
│
├── aws-glue/
│   └── glue_etl_job.py
│
├── sql/
│   └── banking_analytics.sql
│
├── powerbi/
│   └── Banking_Analytics_Dashboard.pbix
│
└── screenshots/
    ├── glue-etl-job.png
    ├── redshift-tables.png
    └── powerbi-dashboard.png

🖼️ Project Screenshots

Add screenshots to the screenshots/ folder.

AWS Glue ETL



Amazon Redshift



Power BI Dashboard



🚀 Complete Project Workflow

1. Generate synthetic banking data
                ↓
2. Upload raw data to Amazon S3
                ↓
3. Build AWS Glue ETL job
                ↓
4. Transform and standardize datasets
                ↓
5. Convert datasets to Parquet
                ↓
6. Store processed data in S3
                ↓
7. Run Glue Crawlers
                ↓
8. Register schemas in Glue Data Catalog
                ↓
9. Load processed data into Redshift Serverless
                ↓
10. Validate data using SQL
                ↓
11. Perform business analytics
                ↓
12. Connect Redshift to Power BI
                ↓
13. Build Power BI data model
                ↓
14. Create DAX measures
                ↓
15. Build Banking Analytics Dashboard

💡 Key Learnings

Built an end-to-end cloud ETL pipeline.

Used Amazon S3 as a cloud storage/data lake layer.

Developed an AWS Glue ETL job.

Worked with Parquet files.

Used AWS Glue Crawlers and Data Catalog.

Loaded analytical data into Amazon Redshift Serverless.

Performed business analysis using SQL.

Used joins, aggregations, CTEs, subqueries, and window functions.

Built a Power BI data model.

Created DAX measures and KPI cards.

Developed a banking analytics dashboard.

Identified and investigated data-quality issues.

⚠️ Data Quality & Security

Data Quality

The project identified non-unique account_id values in the source account dataset. Rather than forcing a many-to-many relationship, the issue was investigated and documented.

A production implementation should add automated validation for:

Duplicate primary keys

Missing foreign keys

Null mandatory fields

Invalid dates

Invalid customer/account relationships

Invalid account/transaction relationships

Security

Never commit the following to GitHub:

AWS access keys

AWS secret keys

Redshift passwords

Database credentials

.env files containing secrets

Private connection strings

Raw banking/customer/card data

🚀 Future Improvements

Add automated data-quality checks in AWS Glue.

Implement incremental ETL processing.

Add workflow orchestration with AWS Step Functions.

Add pipeline monitoring with Amazon CloudWatch.

Implement a dimensional/star schema.

Create a dedicated date dimension.

Add customer segmentation.

Add advanced transaction trend analysis.

Automate Power BI dataset refreshes.

Add CI/CD for ETL scripts.

Introduce Infrastructure as Code using Terraform or CloudFormation.

🎯 Project Value

This project demonstrates practical skills across three areas:

Data Engineering

S3 → Glue → Parquet → Glue Catalog → Redshift

Data Analytics

Redshift → SQL → Business Insights

Business Intelligence

Redshift → Power BI → DAX → Dashboard

The project demonstrates an end-to-end understanding of how data moves from raw source → cloud processing → data warehouse → analytics → business visualization.

👨‍💻 Author

Rathish R

Data Science | Data Analytics | Data Engineering

This project was developed as a hands-on portfolio project to demonstrate practical skills in cloud data engineering, SQL analytics, data modeling, and business intelligence.
