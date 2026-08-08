# 🏦 Banking Data Engineering & Analytics

An end-to-end banking data engineering and analytics project built using **Amazon S3, AWS Glue, Amazon Redshift Serverless, SQL, and Microsoft Power BI**.

The project demonstrates how raw banking data can be transformed through an ETL pipeline, stored in a cloud data warehouse, analyzed using SQL, and visualized through an interactive Power BI dashboard.

---

## 📌 Project Overview

The objective of this project is to build a complete cloud-based data pipeline for a banking dataset.

The pipeline follows:

Raw Data → Amazon S3 → AWS Glue ETL → Parquet → Glue Data Catalog → Amazon Redshift → SQL Analytics → Power BI

The project covers customer, account, branch, transaction, loan, and card information.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │   Synthetic Banking │
                    │       Dataset       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Amazon S3      │
                    │     Raw Data Zone   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      AWS Glue       │
                    │     ETL Pipeline    │
                    └──────────┬──────────┘
                               │
                     Transform & Convert
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Parquet Files    │
                    │   Processed Zone    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Glue Data Catalog │
                    │     & Crawlers      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Amazon Redshift     │
                    │     Serverless      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    SQL Analytics    │
                    │  Business Queries   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Power BI        │
                    │ Analytics Dashboard │
                    └─────────────────────┘
