# Task 1 – Foundational Setup & Exploratory Data Analysis

## Project
Superstore Sales Data Analysis

## Objective
To clean, explore, and analyze the Superstore dataset using Python and identify important patterns, trends, and anomalies.

## Tools Used
- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Data Preparation
- Standardized column names
- Checked missing values and duplicates
- Checked data types and dates
- Detected outliers using the IQR method
- Retained legitimate outlier observations
- Saved the cleaned dataset as `data/processed/superstore_cleaned.csv`

## Exploratory Data Analysis
The analysis includes:
- Statistical summary
- Sales distribution analysis
- Boxplot analysis
- Sales by category
- Sales by region
- Profit by category
- Profit by region
- Sales and profit by customer segment
- Sales vs Profit analysis
- Correlation heatmap

## Key Insights
- Sales are strongly right-skewed.
- Technology records the highest total sales and profit among the categories.
- The West region records the highest total sales and profit.
- The Consumer segment records the highest total sales and profit.
- Sales and profit show a moderate positive correlation.
- Discount and profit show a weak negative correlation.

## Files
- `task1_eda.ipynb` – Jupyter notebook containing the complete analysis
- `data/processed/superstore_cleaned.csv` – cleaned dataset
- `README.md` – project documentation
