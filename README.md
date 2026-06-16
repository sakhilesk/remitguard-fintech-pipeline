<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

    <!-- Project Header -->
    <div align="center">
        <h1>RemitGuard &amp; Retention IQ</h1>
        <h3>🚀 An End-to-End Cloud Data Engineering Platform for Cross-Border Fintech Analytics</h3>
        <p><i>Simulating the data ecosystem of a growth-stage fintech company to optimize user conversion and mitigate customer churn risk.</i></p>
    </div>

    <hr />

    <!-- Project Overview -->
    <h2>📋 Project Overview</h2>
    <p>
        <b>RemitGuard &amp; Retention IQ</b> is a fully functional, production-grade data platform engineered on <b>Microsoft Azure</b>. The platform ingests high-velocity, cross-border remittance transactions and user experience (UX) telemetry logs, moving the data dynamically through a multi-tiered modern data warehouse stack. 
    </p>
    <p>
        The project simulates real-world business challenges faced by fintech platforms like Mama Money, specifically focusing on measuring transaction conversion funnels, enforcing strict data quality protocols, and identifying customer churn signals to protect commercial performance.
    </p>

    <hr />

    <!-- Architecture Section -->
    <h2>🏗️ Architecture &amp; Data Flow</h2>
    <p>
        The modern data warehouse architecture follows an automated ELT (Extract, Load, Transform) design pattern, moving from a raw landing zone to a highly polished business intelligence layer.
    </p>
    
    <!-- PLACEHOLDER FOR ARCHITECTURE DIAGRAM -->
    <div align="center">
        <img src="images/architecture_diagram.png" alt="Data Pipeline Architecture Diagram" width="850" style="border-radius: 8px; border: 1px solid #ddd;" />
        <p><i>Figure 1: End-to-End Data Pipeline Architecture Lifecycle.</i></p>
    </div>

    <ol>
        <li><b>Ingestion Layer:</b> A localized Python application simulates a live transaction microservice, generating synthetic mobile money remittance logs and streaming them directly to cloud infrastructure.</li>
        <li><b>Landing Zone (Bronze):</b> Data lands securely as raw CSV objects in <b>Azure Data Lake Storage Gen2</b>, isolated into structured directories.</li>
        <li><b>Orchestration Layer:</b> <b>Azure Data Factory (ADF)</b> runs time-slice schedules to ingest raw files sequentially into a staging layer.</li>
        <li><b>Data Warehouse Storage:</b> <b>Azure SQL Database</b> hosts the staging area and serves as the compute engine for analytics.</li>
        <li><b>Transformation &amp; Governance (Silver/Gold):</b> <b>dbt (Data Build Tool)</b> executes code to handle analytical modeling, deduplication, and data quality tests natively inside the database.</li>
        <li><b>Business Intelligence:</b> <b>Power BI</b> queries the production-ready analytical marts to surface actionable user growth trends.</li>
    </ol>

    <hr />

    <!-- Tech Stack Section -->
    <h2>🛠️ Tech Stack &amp; Core Frameworks</h2>
    <ul>
        <li><b>Language Stack:</b> Python 3.12+ (Pandas, Faker library, Azure-Storage-Blob Core SDK)</li>
        <li><b>Cloud Infrastructure:</b> Microsoft Azure (Blob Storage/ADLS Gen2, Azure Data Factory, Azure SQL Database)</li>
        <li><b>Transformation Engine:</b> dbt-core v1.8+ using the specialized <code>dbt-sqlserver</code> adapter</li>
        <li><b>Business Intelligence:</b> Power BI Desktop utilizing advanced Data Analysis Expressions (DAX)</li>
    </ul>

    <hr />

    <!-- Step-by-Step Implementation Guide -->
    <h2>🚀 Step-by-Step Implementation</h2>

    <h3>Step 1: Local Ingestion &amp; Azure Blob Upload</h3>
    <p>
        The script <code>generate_and_upload.py</code> dynamically generates realistic transaction records alongside sequential user funnel touchpoints. It establishes a secure TLS session with the cloud resource and streams the data directly to Azure.
    </p>
    
    <!-- PLACEHOLDER FOR VS CODE SCREENSHOT -->
    <div align="center">
        <img src="images/vscode_environment.png" alt="VS Code Python Script Environment" width="800" style="border-radius: 6px; border: 1px solid #ddd;" />
        <p><i>Figure 2: Python Data Generation Environment inside VS Code.</i></p>
    </div>

    <h3>Step 2: Storage Infrastructure Configuration</h3>
    <p>
        The data lake storage accounts are configured with strict hierarchical path structures. Raw files are divided into functional directories representing business telemetry sectors.
    </p>

    <!-- PLACEHOLDER FOR AZURE BLOB STORAGE SCREENSHOT -->
    <div align="center">
        <img src="images/azure_storage_containers.png" alt="Azure Storage Account Containers" width="800" style="border-radius: 6px; border: 1px solid #ddd;" />
        <p><i>Figure 3: Raw CSV data files landing inside Azure Blob Containers.</i></p>
    </div>

    <h3>Step 3: Azure Data Factory (ADF) Automation</h3>
    <p>
        An operational pipeline named <code>pl_ingest_remit_data</code> uses secure SQL and Blob linked service definitions. A copy task maps properties and structure from raw storage strings directly into relational data configurations.
    </p>

    <!-- PLACEHOLDER FOR ADF PIPELINE RUN SCREENSHOT -->
    <div align="center">
        <img src="images/adf_pipeline_success.png" alt="Azure Data Factory Pipeline Execution" width="800" style="border-radius: 6px; border: 1px solid #ddd;" />
        <p><i>Figure 4: Automated copy data workflow run monitor inside Azure Data Factory.</i></p>
    </div>

    <h3>Step 4: Relational Database Initialization</h3>
    <p>
        Tables are defined using optimized transactional data schemas inside the relational cloud instance to capture the incoming staging streams.
    </p>

    <!-- PLACEHOLDER FOR AZURE SQL DATABASE SCREENSHOT -->
    <div align="center">
        <img src="images/azure_sql_tables.png" alt="Azure SQL Database Query Editor Tables" width="800" style="border-radius: 6px; border: 1px solid #ddd;" />
        <p><i>Figure 5: Target tables initialized inside Azure SQL Database Query Editor.</i></p>
    </div>

    <h3>Step 5: High-Performance Data Transformations with dbt</h3>
    <p>
        Using <b>dbt</b>, raw tables are cleaned to prevent common networking duplicates (e.g., duplicate API requests due to mobile signal drops). A window partitioning strategy filters entries to extract and store uniquely valid metrics.
    </p>
    <p>
        Data is then structured into specialized business marts:
    </p>
    <ul>
        <li><code>mart_conversion_funnel</code>: Monitors user retention drop-off paths across payment execution screens.</li>
        <li><code>mart_customer_retention</code>: Segments users into risk profiles based on active transaction activity over a 30-day timeline.</li>
    </ul>

    <!-- PLACEHOLDER FOR DBT RUN SCREENSHOT -->
    <div align="center">
        <img src="images/dbt_run_terminal.png" alt="dbt run and test execution output" width="800" style="border-radius: 6px; border: 1px solid #ddd;" />
        <p><i>Figure 6: Executing data quality validation tests via dbt command line interface.</i></p>
    </div>

    <hr />

    <!-- Visualization Section -->
    <h2>📊 Business Intelligence Layer (Power BI)</h2>
    <p>
        The visualization report layer directly targets production views in the database to build automated dashboards for internal growth groups.
    </p>

    <!-- PLACEHOLDER FOR POWER BI PAGE 1 SCREENSHOT -->
    <div align="center">
        <img src="images/powerbi_conversion_funnel.png" alt="Power BI Conversion Funnel Dashboard" width="850" style="border-radius: 8px; border: 1px solid #ddd;" />
        <p><i>Figure 7: Executive interactive visual of transaction conversion rates.</i></p>
    </div>

    <p>
        <b>Key Analytics Delivered:</b>
    </p>
    <ul>
        <li><b>Conversion Performance Engine:</b> Custom interactive funnel graphics highlight specific dropout points where users drop out between rate calculation and final money transfer steps.</li>
        <li><b>Advanced DAX KPI Cards:</b> Computes critical metrics dynamically at execution runtime:
            <pre><code>Overall Conversion Rate (%) = DIVIDE(SUM(mart_conversion_funnel[total_transfers_completed]), SUM(mart_conversion_funnel[total_app_opens]), 0)</code></pre>
        </li>
        <li><b>Customer Churn Mitigation Matrix:</b> Provides a direct segmentation breakdown highlighting high-risk customer records, enabling direct marketing intervention strategies.</li>
    </ul>

    <hr />

    <!-- Compliance Section -->
    <h2>🔒 Security &amp; Compliance (POPIA / GDPR)</h2>
    <ul>
        <li><b>PII Protection:</b> No authentic, unprotected identity points (e.g., ID numbers, phone fields, names) travel down the stream pipeline; variables are mocked or entirely obfuscated.</li>
        <li><b>Separation of Concerns:</b> General reporting models only have connection privileges to the clean <code>gold</code> warehouse schema views, blocking access to the operational database staging tables.</li>
    </ul>

</body>
</html>
