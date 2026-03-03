# Tulsa Workforce Data Warehouse Prototype

## Project Overview
This project represents the first version of a localized data warehouse for **Tulsa For You and Me**. As a Data Warehouse Engineer, the mission was to standardize messy job and wage data into a structured, scalable model that can power future workforce dashboards and labor market analysis for the Tulsa region.

## Dataset Rationale
We utilized the **O*NET Occupation-Level Database**, specifically the "Occupation Data" tables. 
- **Why?**: These tables provide a high-resolution view of job characteristics (skills, knowledge, and tasks). By standardizing this data, Tulsa can identify skill gaps in the local labor market and align workforce programs with actual industry requirements.

---

## Data Warehouse Schema
The warehouse utilizes a **Star Schema** architecture, designed for high-performance analytical queries. This design separates descriptive attributes (dimensions) from quantitative metrics (facts).

### Table Structure
- **Dimensions** (Descriptive Context):
  - `dim_occupation`: The central entity, containing O*NET-SOC codes, titles, and job descriptions.
  - `dim_skill`: A registry of professional skills tracked across the dataset.
  - `dim_knowledge`: A registry of specialized knowledge domains.
- **Fact Tables** (Quantitative Metrics):
  - `fact_skill_rating`: Captures the **Importance** and **Level** scores of skills for every occupation.
  - `fact_knowledge_rating`: Captures the **Importance** and **Level** scores of knowledge areas for every occupation.

### Schema Diagram (ERD)
![Workforce Warehouse ERD](docs/erd_diagram.png)

---

## ETL Pipeline Logic
Built using **Python (Pandas & DuckDB)**, the pipeline follows a robust 3-stage process:

1.  **Extract**: Ingests raw tab-separated text files from the O*NET database.
2.  **Transform**:
    - **Cleaning**: Standardizes column names (snake_case) for SQL compatibility.
    - **Normalization**: Separates unique skill/knowledge definitions into dimension tables to reduce redundancy.
    - **Pivoting**: O*NET provides scores in a "long" format (multiple rows for IM and LV). The pipeline pivots this into a "wide" format (one row per occupation/skill with two columns) to make analytical joining more efficient.
3.  **Load**: Outputs the structured data into a local **DuckDB** file (`workforce.duckdb`). DuckDB was chosen for its exceptional speed in OLAP (analytical) workloads compared to standard SQLite.

---

## Data Validation
The pipeline includes a dedicated validation suite (`src/validation.py`) to ensure data integrity:
- **Existence Checks**: Verifies that no occupation title is missing (NULL).
- **Uniqueness**: Ensures that the granularity of fact tables is correct (no duplicate occupation-skill pairs).
- **Referential Integrity**: Confirms that every skill/knowledge rating in a fact table has a corresponding entry in the dimension table.
- **Domain Constraints**: Validates that all "Importance Scores" fall within the standard O*NET range (0 to 5).

---


---

## Getting Started
### Setup
1. **Create Environment**: `python -m venv venv`
2. **Activate**: `.\venv\Scripts\activate` (Windows)
3. **Install**: `pip install -r requirements.txt`

### Execution
- **Run Pipeline**: `python src/etl.py`
- **Run Validation**: `python src/validation.py`
- **Run Insights**: `python src/run_queries.py`

---
## Video Walkthrough
https://www.loom.com/share/a9eb78a7f6af4e28a67c41f931e2e411
*(In the walkthrough, I cover the schema design rationale, demonstrate the ETL transition from raw text to DuckDB, and walk through the 'Most Cross-Functional Skills' query.)*
