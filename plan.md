12-Week Power BI & Data Engineering Career Project

Overview
- Goal: Build an end-to-end, cloud-aligned portfolio project covering data ingestion, transformation, modeling, BI delivery (Power BI), data quality, CI/CD, and project management roleplay. Emphasizes Azure and AWS tradeoffs while minimizing costs using local tools (DuckDB, dbt-core, GitHub Actions).
- Outcomes: GitHub repo with code, CI templates, documented skills matrix (hard vs meta), two agent prompts (skill-doc and PM), and a recorded demo/slide deck.

Week-by-week plan

Week 1 — Project setup & Git
- Objectives: Initialize GitHub repo, learn branching, PR workflow, basic CI. Set up local dev environment (Python, dbt-core, DuckDB), Power BI Desktop.
- Deliverables: GitHub repo skeleton, README, .gitignore, simple CI that lints Python and runs a smoke test.
- Skills: Git/GitHub, GitHub Actions, repo organization (meta), environment setup (hard).

Week 2 — SQL & Data Modeling
- Objectives: Master SQL (Joins, window functions), dimensional modeling (star schema), and writing analytics-friendly schemas.
- Deliverables: SQL workshop notebook, dimensional model for sample domain (sales/transactions), sample queries.
- Skills: SQL, data modeling, problem decomposition (hard); documentation (meta).

Week 3 — Power BI Modeling & DAX
- Objectives: Build semantic model in Power BI Desktop, master calculated columns, measures, and performance tuning.
- Deliverables: PBIX with modeled dataset, 5 key DAX measures, model documentation.
- Skills: Power BI Desktop, DAX, performance tuning (hard); stakeholder storytelling (meta).

Week 4 — Ingestion: Azure & Cost-free alternatives
- Objectives: Ingest sample data from APIs/files using Azure Data Factory (overview) and local alternatives (Python scripts, Airbyte if possible). Learn Azure storage basics (Blob) and S3 for AWS.
- Deliverables: ADF pipeline skeleton (ARM or Bicep template stub), Python ingestion scripts pushing to local DuckDB/CSV, instructions to run.
- Skills: Azure Data Factory concepts, Blob/S3, Python ETL (hard); infra-as-code basics (meta).

Week 5 — Orchestration & Scheduling
- Objectives: Implement workflow orchestration with Airflow (local via Docker) or Azure Data Factory triggers and GitHub Actions for scheduling.
- Deliverables: Local Airflow DAGs or ADF trigger examples; CI job to run end-to-end pipeline on push.
- Skills: Orchestration (Airflow/ADF), scheduling, parameterization (hard); reliability mindset (meta).

Week 6 — Data Warehouse & Storage
- Objectives: Implement analytical warehouse layer using DuckDB or a free Postgres/Docker instance; learn cloud options (Synapse/Snowflake overview).
- Deliverables: Warehouse schema, nightly load job, simple partitioning strategy documented.
- Skills: Warehousing concepts, partitioning, cost tradeoffs (hard); architectural tradeoff docs (meta).

Week 7 — Transformations with dbt
- Objectives: Learn dbt-core (with DuckDB backend), write models, tests, docs, and use versioned models.
- Deliverables: dbt project with models, schema tests, generated docs site (locally), CI test job.
- Skills: dbt, SQL transformations, testing, docs (hard); CI integration (meta).

Week 8 — Data Quality & Observability
- Objectives: Add data tests (dbt + Great Expectations), implement monitoring alerts (GitHub Actions for test failures), basic lineage documentation.
- Deliverables: GE suites or dbt tests, alerting playbook, runbook for data incidents.
- Skills: Data quality frameworks, observability, runbooks (hard); incident communication (meta).

Week 9 — Power BI Service & Deployment
- Objectives: Publish to Power BI Service (Pro trial), set refresh schedules, explore deployment pipelines (ALM) and dataset lifecycle; simulate semantic layer with Power BI datasets.
- Deliverables: Published report, scheduled refresh configured, docs on ALM (deployment pipelines) and limitations without Premium.
- Skills: Power BI Service, dataset refresh, ALM concepts (hard); user adoption strategies (meta).

Week 10 — CI/CD & Infra-as-Code
- Objectives: Implement GitHub Actions for CI (lint/tests) and CD (deploy artifacts). Introduce Terraform or ARM/Bicep basics for infra stubs.
- Deliverables: CI pipelines, sample CD workflow to deploy dbt docs and run tests; IaC templates stubbed.
- Skills: GitHub Actions CI/CD, Terraform/ARM (meta and hard).

Week 11 — Governance, Security & Cataloging
- Objectives: Document data governance: access controls, PII handling, data lineage. Explore Data Catalog tools (Atlan/DataHub) and Azure Purview overview.
- Deliverables: Governance policy doc, sample RBAC configs, metadata catalog (README + tags).
- Skills: Data governance, security best practices, metadata (hard); policy writing (meta).

Week 12 — Capstone & Portfolio
- Objectives: Complete end-to-end demo, produce slide deck and recorded walkthrough, prepare interview artifacts (one-pager, README explaining decisions and tradeoffs).
- Deliverables: Demo video, final README, public GitHub repo, portfolio writeup mapping work to job requirements.
- Skills: Presentation, storytelling, stakeholder demos (meta); full-stack data engineering and BI (hard).

Stretch goals
- Add streaming: Kafka/Kinesis sample (Quanata-relevant).
- Try Snowflake or Synapse trial, Power BI Premium/Fabric trial when accessible.

Next steps (now)
1. Confirm and I'll create the GitHub repo skeleton, CI templates, and agent prompts.
2. If confirmed, files will be committed in your workspace and session files; weekly check-ins and task lists will be created.

