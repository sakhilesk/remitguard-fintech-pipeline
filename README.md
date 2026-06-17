# RemitGuard & Retention IQ: Cross-Border Fintech Data Platform

An end-to-end cloud data engineering platform designed to ingest, orchestrate, transform, and visualize cross-border remittance transactions and user experience (UX) telemetry logs. This project closely mirrors the production data ecosystem of a high-growth fintech platform (such as Mama Money), focusing heavily on analytical data quality, customer conversion funnels, and automated retention matrices.

---

## 🏗️ Architecture & Data Flow

The platform utilizes a modern cloud data stack built entirely on Microsoft Azure, leveraging programmatic data generation, automated orchestration pipelines, robust ELT warehouse transformations, and executive business intelligence reporting.

[In-Memory Data Generator] ➡️ [Azure Blob Storage (Bronze)] ➡️ [Azure Data Factory]
⬇️
[Power BI Dashboards (Gold)] ⬅️ [dbt Core Transformations (Silver/Gold)] ⬅️ [Azure SQL DB (Staging)]

1. **Ingestion Layer:** A local Python script simulating transactional and application microservices generates randomized fintech event streams and uploads them as CSV payloads directly into cloud storage via the `azure-storage-blob` SDK.
2. **Landing Zone (Bronze):** Azure Storage Account configured with hierarchical namespaces to separate data streams into distinct operational directories (`/transactions` and `/ux-logs`).
3. **Orchestration Layer:** Azure Data Factory (ADF) handles job scheduling, connection strings, and automated data ingestion.
4. **Data Warehouse (Staging):** Azure SQL Database acts as the centralized relational compute engine, initially hosting raw landing tables.
5. **Transformation & Quality Layer:** `dbt-core` connected via the `dbt-sqlserver` adapter manages modular SQL modeling, schema isolation, and automated data quality constraints.
6. **Visualization Layer:** Power BI Desktop establishes a dedicated gateway to the warehouse to expose self-service analytics to product and growth teams.

---

 🛠️ Tech Stack & Key Frameworks
* **Language:** Python 3.12+ (Pandas, Faker, Azure-Storage-Blob)
* **Cloud Infrastructure:** Microsoft Azure (Blob Storage, Azure Data Factory, Azure SQL Database)
* **Transformation & Governance:** dbt (Data Build Tool) / `dbt-sqlserver`
* **Business Intelligence:** Power BI (DAX, Interactive Reporting)

---

## 🚀 Step-by-Step Project Implementation

### Step 1: Programmatic Data Mocking & Azure Ingestion
The Python script `generate_and_upload.py` acts as our operational source layer. It creates 150 transaction batches alongside their respective UX application journey steps, mapping corridors across regional African borders, and uploads them to the cloud.

```bash
# Install dependencies
pip install pandas faker azure-storage-blob

# Execute the ingestion pipeline script
python generate_and_upload.py

Step 2: Relational Warehouse Preparation
Before moving data, the destination Azure SQL Database initializes an isolated schema to safely contain incoming data streams before transformation.

CREATE SCHEMA staging;
GO

CREATE TABLE staging.raw_transactions (
    transaction_id VARCHAR(50),
    sender_id VARCHAR(50),
    source_country VARCHAR(50),
    destination_country VARCHAR(50),
    amount_zar DECIMAL(18, 2),
    exchange_rate DECIMAL(18, 4),
    status VARCHAR(20),
    timestamp DATETIME
);
GO

Step 3: Azure Data Factory (ADF) Ingestion Workflow
Within Azure Data Factory, automated data pipelines are established using distinct connection pathways:

Linked Services: ls_blob_remitguard (Secure Access Key Auth) and ls_sqldb_remitguard (SQL Database Authentication).

Pipeline Logic (pl_ingest_remit_data): Consists of sequential Copy Data Activities. A green success constraint link is configured so that the UX logs are only ingested if the transactional data loads successfully, preserving cross-table analytical integrity.

Step 4: Analytical Modeling & Data Cleansing (dbt)
The warehouse transitions raw data into structured, clean schemas using a multi-tiered modeling approach within dbt.

Silver Layer (Deduplication & Schema Enforcement)
To handle potential network retries or duplicate entries common in digital remittance transfers, a SQL window function filters out duplicate payloads, ensuring that only the latest unique record passes into the analytical layer:

-- silver_transactions.sql
{{ config(schema='silver') }}

WITH ranked_transactions AS (
    SELECT 
        *, 
        ROW_NUMBER() OVER (PARTITION BY transaction_id ORDER BY timestamp DESC) as row_num
    FROM {{ source('azure_staging', 'raw_transactions') }}
)
SELECT 
    transaction_id, 
    sender_id, 
    UPPER(destination_country) as destination_country, 
    amount_zar, 
    transaction_status, 
    transaction_at
FROM ranked_transactions 
WHERE row_num = 1

Gold Layer (Business Value Data Marts)
mart_conversion_funnel: Aggregates application events to trace customer journey drops and completion cycles.

mart_customer_retention: Evaluates active sending cycles and tracks customer inactivity past a 30-day window to identify churn risk.

Step 5: Data Quality Testing & Governance
Data integrity constraints are strictly enforced using native dbt test suites before any tables are exposed to business intelligence users.

# models/schema.yml
version: 2
models:
  - name: silver_transactions
    columns:
      - name: transaction_id
        tests:
          - unique
          - not_null

# Compile code into Azure SQL and trigger data validation audits
dbt run
dbt test

📊 Business Intelligence & Self-Service Insights
                                                       Link to the Dashboard
                 https://app.powerbi.com/links/UDrCzpWB_j?ctid=51998145-5b74-4c67-a4bc-653fc4af7795&pbi_source=linkShare

The visualization layer connects straight to the Gold Schema inside Azure SQL Database. It is structured around two interactive dashboards built to help teams prioritize people and product improvements:

1. User Experience Onboarding & Funnel Analytics
Tracks customer velocity and drop-offs across the transaction flow (App Open ➡️ Rate Calculated ➡️ Transfer Initiated ➡️ Transfer Settled).

Implements native, lightweight DAX Card Measures to showcase performance at a glance, keeping the compute load on the warehouse minimal:

Overall Conversion Rate (%) = 
DIVIDE(
    SUM(mart_conversion_funnel[total_transfers_completed]), 
    SUM(mart_conversion_funnel[total_app_opens]), 
    0
)

2. Retention Analytics & Churn Matrix
Implements a segmentation matrix categorizing active regional senders into actionable lifecycle buckets: Active / Safe, Medium Risk, and High Churn Risk.

Displays a dedicated workspace listing specific sender_id references flagged as high churn risks, giving marketing and growth teams a direct list of users to contact with support or targeted promotional campaigns.

🔒 Security & Compliance Principles
Data Minimization: No real or unhashed Personally Identifiable Information (PII) such as phone numbers, banking data, or real names are generated or stored, completely aligning with POPIA (South Africa) and GDPR compliance.

Separation of Concerns: End users and BI platforms are restricted exclusively to the gold data schema views, protecting operational staging layers from external query overhead or exposure.
