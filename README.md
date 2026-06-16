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
