# E-commerce-Analytics-Pipeline-using-FakeStore-API

E-Commerce Data Pipeline (FakeStore API)

Python | API Extraction | Data Cleaning | Analysis | Automation | SQLite | CSV

📌 1. Project Overview

This project is an end-to-end data pipeline built using Python to extract, clean, analyze, and store real-time product data from the FakeStore REST API.

It is designed to demonstrate practical skills required for:

-Python Developer

-Data Analyst

-Data Engineer (L1)

-Automation Engineer

This pipeline mimics a mini real-world ETL workflow:

Extract → Transform → Analyze → Load → Automate

The project outputs:

1. A clean CSV file

2. A SQLite database

3. A text-based analysis report

4. Logging + modular code structure for production-like behavior

📌 2. Why This Project? (Problem Statement)

Modern businesses rely heavily on real-time product analytics:

-E-commerce companies need pricing insights

-Analysts track category performance

-Engineers automate data collection pipelines

-Websites require scraping or API ingestion workflows

However, most beginner projects only show:
❌ standalone notebooks
❌ small scripts
❌ no modular design
❌ no database storage
❌ no automation

This project solves that by showcasing a professional pipeline that can scale, be reused, and be extended — just like one in a real job.

📌 3. Project Features
🔹 1. API Data Extraction

Fetches product data using the FakeStore API

Includes retry logic, error handling, and logging

Validates and returns consistent JSON output

🔹 2. Data Transformation

Cleans missing values

Normalizes categories

Flattens nested fields (like rating)

Adds new derived features:

price_with_tax

title_length

category_avg_price

🔹 3. Exploratory Data Analysis

Generates insights such as:

Number of products

Category distribution

Cheapest & costliest items

Highest average price category

Useful for dashboards and reporting

🔹 4. Storage (Load Layer)

Stores results in:

✔ CSV (products.csv)
✔ SQLite DB (products.db)

Great for Data Engineering roles.

🔹 5. Modular Code Structure
src/
 ├── extract.py      → API extraction
 ├── transform.py    → Data cleaning & engineering
 ├── analysis.py     → Insight generation
 └── load.py         → CSV + SQLite storage
main.py              → Pipeline orchestrator

🔹 6. Extensible Architecture

You can easily plug in:

Cron jobs

Airflow

Power BI dashboards

Machine learning models

📌 4. Tech Stack

Python

Pandas

Requests

SQLite3

Logging

Modular OOP-ready architecture

REST API integration

📌 5. Dataset Source

Data is sourced from FakeStore API:
https://fakestoreapi.com/products

This provides real-like e-commerce product data including:

Titles

Prices

Categories

Descriptions

Ratings (nested JSON)

📌 6. Project Architecture
                      +----------------------+
                      |     FakeStore API    |
                      +----------+-----------+
                                 |
                                 ▼
                      +----------------------+
                      |    Extract Layer     |
                      |  (extract.py)        |
                      +----------------------+
                                 |
                                 ▼
                      +----------------------+
                      |   Transform Layer    |
                      |  (transform.py)      |
                      +----------------------+
                                 |
                                 ▼
                      +----------------------+
                      |     Analysis Layer   |
                      |   (analysis.py)      |
                      +----------------------+
                                 |
                                 ▼
            +----------------------------+-----------------------------+
            |                            |                             |
            ▼                            ▼                             ▼
   +----------------+          +----------------+            +------------------+
   |   CSV Output   |          | SQLite DB      |            | summary.txt      |
   +----------------+          +----------------+            +------------------+

📌 7. How to Run This Project
🔧 Step 1: Install Dependencies
pip install requests pandas

🔧 Step 2: Run the Pipeline
python main.py

🔧 Step 3: Outputs Created

After running, you’ll see an output/ folder created with:

✔ products.csv
✔ products.db
✔ summary.txt

📌 8. Sample Output (summary.txt)
Total products: 20
Number of categories: 4
Highest avg price category: Electronics
Cheapest product: Men's Cotton Jacket ($55.99)
Most expensive product: Samsung 49-Inch Monitor ($999.99)

📌 9. What This Project Demonstrates in Interviews
✔ Python Developer Skills

API requests

Modular code

Error handling

Logging

✔ Data Analyst Skills

Data cleaning

Feature engineering

Insights generation

CSV reporting

✔ Data Engineer Skills

ETL pipeline design

SQLite database load

Folder structure & orchestration

Scalability

✔ Automation Skills

Pipeline building

Reusable functions

Configurable retry logic

You can confidently talk about this project in ANY tech interview.

📌 10. Future Enhancements

Integrate scheduling (Cron/Airflow)

Build a Power BI dashboard on top of SQLite

Add product sentiment analysis using scraped reviews

Push data to a cloud warehouse (BigQuery, Snowflake)

Convert pipeline into an API using FastAPI

📌 11. Author

Hritika Ranadhir
Python | SQL | Data Analyst | Data Engineer
📍 Pune, India
💼 LinkedIn: linkedin.com/in/hritika-ranadhir
💻 GitHub: github.com/HritikaRanadhir02
