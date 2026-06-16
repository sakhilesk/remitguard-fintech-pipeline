<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Repository Setup Guide</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292f;
            background-color: #f6f8fa;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: #ffffff;
            padding: 40px;
            border: 1px solid #d0d7de;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(27,31,35,0.12);
        }
        h1 {
            font-size: 2rem;
            border-bottom: 1px solid #d0d7de;
            padding-bottom: 10px;
            color: #0969da;
        }
        h2 {
            font-size: 1.5rem;
            border-bottom: 1px solid #d0d7de;
            padding-bottom: 8px;
            margin-top: 24px;
        }
        h3 {
            font-size: 1.25rem;
            margin-top: 20px;
        }
        code {
            font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;
            background-color: rgba(175,184,193,0.2);
            padding: 0.2em 0.4em;
            border-radius: 6px;
            font-size: 85%;
        }
        pre {
            background-color: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
            border: 1px solid #d0d7de;
        }
        pre code {
            background-color: transparent;
            padding: 0;
            border-radius: 0;
            font-size: 100%;
            color: #24292f;
        }
        ul, ol {
            padding-left: 2em;
        }
        li {
            margin-top: 0.25em;
        }
        .placeholder-box {
            background-color: #fff8c5;
            border: 1px dashed #9a6700;
            padding: 15px;
            border-radius: 6px;
            margin: 15px 0;
            font-style: italic;
            color: #765a00;
        }
        .tag {
            background-color: #ddf4ff;
            color: #0969da;
            padding: 4px 8px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            display: inline-block;
            margin-right: 5px;
            margin-bottom: 5px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>GitHub Repository Configuration Dashboard</h1>
    <p>This document contains all the text structures, settings, and code formatting you need to populate your GitHub repository for the <strong>remitguard-fintech-pipeline</strong> project.</p>
    
    <hr>

    <h2>1. Repository Metadata Settings</h2>
    <p><strong>Repository Name:</strong> <code>remitguard-fintech-pipeline</code></p>
    <p><strong>Description:</strong></p>
    <pre>An end-to-end cloud data pipeline built on Azure, dbt, and Power BI simulating a cross-border fintech platform to analyze customer conversion funnels and churn risks.</pre>
    
    <p><strong>Repository Topics (Tags):</strong></p>
    <div>
        <span class="tag">azure</span>
        <span class="tag">dbt</span>
        <span class="tag">powerbi</span>
        <span class="tag">data-engineering</span>
        <span class="tag">fintech</span>
        <span class="tag">python</span>
        <span class="tag">etl-pipeline</span>
        <span class="tag">azure-data-factory</span>
    </div>

    <h2>2. Repository Directory Structure</h2>
    <p>Organize your files in VS Code to look exactly like this before your final push:</p>
    <pre>
remitguard-fintech-pipeline/
│
├── .gitignore
├── README.md
│
├── src/
│   └── generate_and_upload.py         # Python Data Generation Script
│
└── remitguard_transforms/             # Your Core dbt Project Folder
    ├── dbt_project.yml
    ├── profiles.yml                   # Keep credentials out or use placeholders
    ├── models/
    │   ├── sources.yml
    │   ├── schema.yml
    │   ├── silver_transactions.sql
    │   ├── silver_ux_logs.sql
    │   ├── mart_conversion_funnel.sql
    │   └── mart_customer_retention.sql
    └── target/
    </pre>

    <h2>3. Production-Ready README.md Content</h2>
    <p>Copy the entire raw markdown block below into your <code>README.md</code> file. Placeholders are noted where you can insert your screenshots after taking them.</p>

    <pre><code># RemitGuard &amp; Retention IQ: Cross-Border Fintech Analytics Platform

An end-to-end cloud data engineering platform designed to ingest, orchestrate, clean, and visualize cross-border remittance transactions and user experience (UX) telemetry logs. This project simulates the data ecosystem of a growth-stage fintech company like Mama Money, focusing heavily on operational data quality, customer conversion funnels, and retention analytics.

---

## 🏗️ Architecture Overview

The platform utilizes a modern cloud data stack built entirely on Microsoft Azure, leveraging programmatic data generation, automated orchestration, robust ELT transformations, and business intelligence reporting.

&lt;!-- PLACE YOUR ARCHITECTURE DIAGRAM OR VSCODE WORKSPACE SCREENSHOT HERE --&gt;
### VS Code Development Environment
![VS Code Workspace Setup](https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?q=80&w=1000&auto=format&fit=crop) *(Replace this placeholder image with your VS Code Screenshot)*

1. **Ingestion Layer:** A localized Python script simulating a transactional microservice generates randomized fintech streams and uploads them as CSVs directly into cloud storage via the Azure Blob SDK.
2. **Landing Zone:** Azure Data Lake Storage (ADLS Gen2) structured into distinct folders acting as a Bronze storage environment.
3. **Orchestration Layer:** Azure Data Factory (ADF) handles scheduling, connection management, and copies data into a relational database.
4. **Data Warehouse (Staging):** Azure SQL Database acts as the relational storage engine hosting our raw schemas.
5. **Transformation &amp; Testing Layer:** `dbt-core` connected via the `dbt-sqlserver` adapter manages the data pipelines into cleanly modeled Silver and Gold layers.
6. **Visualization Layer:** Power BI Desktop establishes a direct gateway to the data warehouse to expose executive analytical dashboards.

---

## 🛠️ Tech Stack &amp; Key Frameworks
* **Language:** Python 3.12+ (Pandas, Faker, Azure-Storage-Blob)
* **Cloud Infrastructure:** Microsoft Azure (Blob Storage, Azure Data Factory, Azure SQL Database)
* **Transformation &amp; Data Governance:** dbt (Data Build Tool) v1.8+ / `dbt-sqlserver`
* **Business Intelligence:** Power BI (DAX, Interactive Reporting)

---

## 🚀 Step-by-Step Implementation Guide

### Step 1: Data Generation &amp; Azure Storage Upload
The Python script `generate_and_upload.py` simulates production app activities. It mocks 150 transaction batches alongside their respective UX application journey steps and establishes an authenticated session over TLS to upload them to the Azure Blob Container.

&lt;!-- INSERT YOUR AZURE STORAGE BLOB CONTAINER SCREENSHOT HERE --&gt;
### Azure Storage Landing Zone (Bronze Data)
*Insert screenshot of your Azure storage container showing the transactions and ux-logs folders here.*

### Step 2: Data Warehouse Initialization
Our target Azure SQL Database initializes a designated `staging` landing area to receive high-velocity data before processing.

&lt;!-- INSERT YOUR AZURE SQL DATABASE / QUERY EDITOR SCREENSHOT HERE --&gt;
### Target Relational Database Tables
*Insert screenshot of your Azure SQL Database showing the raw tables or your DDL queries here.*

### Step 3: Azure Data Factory Orchestration
Within Azure Data Factory, automated extraction routes are mapped using custom linked endpoints:
* **Linked Services:** `ls_blob_remitguard` (SAS/Access Key Authentication) and `ls_sqldb_remitguard` (SQL Auth secure connection).
* **Pipeline Flow (`pl_ingest_remit_data`):** A coordinated data-movement execution plan utilizing a sequential constraint rule that triggers `copy_ux_logs` only upon the successful completion of the `copy_transactions` activity.

&lt;!-- INSERT YOUR AZURE DATA FACTORY PIPELINE MONITOR SCREENSHOT HERE --&gt;
### Orchestration Control Flow (ADF Success Run)
*Insert screenshot of your successful pipeline canvas or your monitor dashboard indicating successful ingestion runs here.*

### Step 4: Analytical Data Transformations (dbt)
The warehouse transitions raw data into a dimensional data structure using a multi-tiered layer approach in `dbt`.

#### Silver Layer (Deduplication &amp; Cleansing)
To combat network retry duplicates common in cross-border environments, window functions filter incoming traffic to guarantee unique transaction IDs:

```sql
WITH ranked_transactions AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY transaction_id ORDER BY timestamp DESC) as row_num
    FROM {{ source('azure_staging', 'raw_transactions') }}
)
SELECT transaction_id, sender_id, UPPER(destination_country) as destination_country, amount_zar, transaction_status
FROM ranked_transactions WHERE row_num = 1
