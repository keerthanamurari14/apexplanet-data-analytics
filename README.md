# Superstore Sales Data Analysis

**ApexPlanet Data Analytics Internship – Tasks 1 to 5**

## Project Overview
This project analyzes the Sample Superstore dataset to understand sales, profit, customer behavior, regional performance, and business trends.

## Dataset
- Records: 10,194
- Columns: 21
- Cleaned dataset: `data/processed/superstore_cleaned.csv`

## Tasks Completed

### Task 1 – Data Cleaning and Exploratory Data Analysis
- Standardized column names and checked data types.
- Checked missing values and duplicate records.
- Examined outliers using the IQR method.
- Analyzed sales, profit, categories, regions, and customer segments.

### Task 2 – SQL and Python Analysis
- Performed SQL-based analysis.
- Used Python notebooks and scripts for database-related work.
- SQL queries: `scripts/task2_queries.sql`.

### Task 3 – Data Visualization
- Created visualizations for sales and profit trends.
- Saved a Tableau dashboard backup.
- Created a monthly sales trend visualization.

### Task 4 – Advanced Analytics
- Performed descriptive statistics and hypothesis testing.
- Evaluated forecasting models.
- Applied K-Means customer segmentation.
- Built regression and classification models.

### Task 5 – Automation and Final Reporting
- Automated KPI calculations using Python.
- Exported results to CSV and Excel.
- Generated a final PDF analytics report.

## Key Findings
- Technology recorded the highest total sales and profit among categories.
- The West region recorded the highest total sales and profit.
- The Consumer segment recorded the highest total sales and profit.
- Sales showed a strongly right-skewed distribution.
- Discounted transactions had lower average profit than non-discounted transactions.
- Decision Tree regression performed better than Linear Regression in the evaluated test set.
- Exponential Smoothing had the lowest forecast errors among the evaluated forecasting models.

## Technologies Used
- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Jupyter Notebook
- SQL
- Tableau
- Scikit-learn
- Statsmodels
- ReportLab
- OpenPyXL

## Project Structure
```text
apexplanet-data-analytics/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── scripts/
├── dashboards/
├── reports/
├── requirements.txt
└── README.md
```

## How to Run
1. Clone the repository:
   `git clone https://github.com/keerthanamurari14/apexplanet-data-analytics.git`
2. Enter the project directory:
   `cd apexplanet-data-analytics`
3. Create and activate a virtual environment:
   `python3 -m venv .venv`
   `source .venv/bin/activate`
4. Install dependencies:
   `pip install -r requirements.txt`
5. Run the KPI automation:
   `python scripts/automate_analysis.py`
6. Open the notebooks:
   `jupyter notebook`

## Main Deliverables
- Notebooks for Tasks 1–4.
- Cleaned dataset.
- SQL queries and Python scripts.
- Tableau dashboard backup and visualization files.
- KPI automation CSV and Excel outputs.
- Final PDF analytics report.

## Author
**Keerthana Murari**

GitHub: https://github.com/keerthanamurari14  
LinkedIn: https://www.linkedin.com/in/murari-sai-keerthana-213bb63aa

## Dashboard

[View Interactive Tableau Dashboard](https://public.tableau.com/app/profile/keerthana.murari/viz/ApexPlanetSuperstoreSalesAnalysis/ExecutiveSalesDashboardSuperstoreSalesAnalysis)
