from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak,
    Table, TableStyle, KeepTogether
)
from reportlab.lib.enums import TA_CENTER
import os
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "reports", "Final_Superstore_Analytics_Report.pdf")
CHART_DIR = os.path.join(ROOT, "reports", "python_charts")

os.makedirs(os.path.dirname(OUT), exist_ok=True)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", parent=styles["Title"], fontSize=25,
    leading=32, textColor=colors.HexColor("#17365D"),
    alignment=TA_CENTER, spaceAfter=18
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading1"], fontSize=16,
    textColor=colors.HexColor("#17365D"), spaceBefore=14,
    spaceAfter=9
))
styles.add(ParagraphStyle(
    name="SubSection", parent=styles["Heading2"], fontSize=12,
    textColor=colors.HexColor("#2874A6"), spaceBefore=9,
    spaceAfter=5
))
styles.add(ParagraphStyle(
    name="Small", parent=styles["BodyText"], fontSize=8,
    leading=11
))

doc = SimpleDocTemplate(
    OUT, pagesize=A4, rightMargin=48, leftMargin=48,
    topMargin=48, bottomMargin=48
)
story = []

def p(text, style="BodyText"):
    story.append(Paragraph(text, styles[style]))
    story.append(Spacer(1, 7))

def heading(text):
    p(text, "Section")

def table(rows, widths=None):
    t = Table(rows, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17365D")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, colors.HexColor("#EAF2F8")]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

def footer(canvas, document):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(48, 25, "Superstore Sales Data Analysis | ApexPlanet Internship")
    canvas.drawRightString(A4[0] - 48, 25, f"Page {document.page}")
    canvas.restoreState()

# Cover
story.append(Spacer(1, 1.0 * inch))
p("FINAL PROJECT REPORT", "CoverTitle")
p("SUPERSTORE SALES DATA ANALYSIS", "CoverTitle")
p("ApexPlanet Data Analytics Internship", "Heading2")
story.append(Spacer(1, 20))
p("<b>Project:</b> Superstore Sales Data Analysis")
p("<b>Tools:</b> Python, Pandas, Matplotlib, Seaborn, SQL, Tableau, Scikit-learn")
p("<b>Dataset:</b> Sample Superstore")
p("<b>Report scope:</b> Tasks 1–4")
story.append(Spacer(1, 30))
p("Prepared as the final reporting deliverable for the data analytics project.", "Small")
story.append(PageBreak())

# Contents
heading("Table of Contents")
for item in [
    "1. Executive Summary", "2. Problem Statement and Objectives",
    "3. Dataset and Methodology", "4. Data Cleaning and Exploratory Analysis",
    "5. SQL Analysis and Visualisation", "6. Statistical Analysis",
    "7. Time-Series Forecasting", "8. Customer Segmentation",
    "9. Machine Learning Results", "10. Findings and Recommendations",
    "11. Limitations and Future Scope", "12. Conclusion"
]:
    p(item, "BodyText")
story.append(PageBreak())

heading("1. Executive Summary")
p(
    "This project analyses the Sample Superstore dataset to understand sales, "
    "profitability, customer behaviour and business performance. The work "
    "covers data preparation, exploratory data analysis, SQL-based analysis, "
    "visualisation, statistical testing, time-series forecasting, customer "
    "segmentation and predictive modelling."
)
p(
    "The analysis found substantial variation in sales and profit, a "
    "significant difference in profit between discounted and non-discounted "
    "transactions, and useful customer groups with different purchasing "
    "and profitability patterns. Among the tested forecasting models, "
    "Exponential Smoothing produced the lowest holdout errors."
)
p(
    "The results can support better discount decisions, customer retention, "
    "product planning and sales monitoring. The findings describe patterns "
    "in the available dataset and should not automatically be interpreted "
    "as causal relationships."
)

heading("2. Problem Statement and Objectives")
p(
    "<b>Problem statement:</b> Understand the factors associated with "
    "Superstore sales and profitability and identify useful patterns "
    "that can support business decisions."
)
p("<b>Objectives:</b>")
for x in [
    "Prepare and clean the dataset for analysis.",
    "Explore sales, profit, quantity, discount and customer patterns.",
    "Use SQL queries to retrieve and analyse business information.",
    "Create visualisations and an interactive dashboard.",
    "Apply statistical tests and time-series forecasting.",
    "Segment customers and evaluate predictive machine-learning models.",
    "Present actionable recommendations based on the findings."
]:
    p("• " + x)

heading("3. Dataset and Methodology")
p(
    "The project uses the Sample Superstore dataset. The raw Excel file is "
    "stored in data/raw/sample_-_superstore.xls and the cleaned dataset is "
    "stored in data/processed/superstore_cleaned.csv."
)
p(
    "The workflow includes data inspection, cleaning, exploratory analysis, "
    "SQL querying, visualisation, statistical testing, forecasting, "
    "segmentation and model evaluation."
)

heading("4. Data Cleaning and Exploratory Analysis")
p(
    "The preparation work included standardising column names, checking "
    "missing values and duplicates, reviewing data types and dates, and "
    "examining outliers using the IQR method. Legitimate outlier observations "
    "were retained."
)
p(
    "The exploratory analysis examined sales distribution, category and "
    "regional performance, profit patterns, customer segments, sales versus "
    "profit and correlations."
)
p(
    "<b>Recorded EDA observations:</b> Sales are strongly right-skewed. "
    "Technology records the highest total sales and profit among categories. "
    "The West region and Consumer segment record the highest total sales "
    "and profit in the initial analysis."
)

heading("5. SQL Analysis and Visualisation")
p(
    "Task 2 used SQL queries and Python integration for structured data "
    "analysis. The SQL query file is available at scripts/task2_queries.sql. "
    "Database helper scripts are stored in scripts/."
)
p(
    "Task 3 developed visualisations and a Tableau dashboard. The project "
    "contains dashboards/Task3_Final_Dashboard_Backup.twbx and the "
    "monthly sales trend HTML visualisation. The dashboard should be "
    "opened in Tableau to review its interactive elements."
)

heading("6. Statistical Analysis")
p(
    "The Task 4 analysis calculated descriptive statistics and confidence "
    "intervals and conducted hypothesis tests."
)
table([
    ["Measure", "Mean", "Median", "Standard deviation"],
    ["Sales", "228.226", "53.91", "619.907"],
    ["Quantity", "3.792", "3", "2.228"],
    ["Discount", "0.155", "0.20", "0.206"],
    ["Profit", "28.673", "8.69", "232.465"],
])
p("The 95% confidence interval for mean Sales was 216.19 to 240.26.")
table([
    ["Test", "Result", "Interpretation"],
    ["Discounted vs non-discounted profit",
     "t = 15.8941; p = 3.73 × 10⁻⁵⁶",
     "Statistically significant difference"],
    ["Segment vs Region",
     "χ² = 6.1988; p = 0.4013",
     "No significant association detected"],
    ["Profit across Segments",
     "F = 0.9414; p = 0.3901",
     "No significant mean difference detected"],
])
p(
    "Average profit was 66.34 for non-discounted transactions and -6.53 "
    "for discounted transactions. This is an observed association and "
    "does not establish that discounts alone caused the difference."
)

heading("7. Time-Series Forecasting")
p(
    "The monthly sales series contained 48 observations from January 2023 "
    "through December 2026, with total sales of 2,326,534.35. The Augmented "
    "Dickey-Fuller test returned a statistic of -4.4375 and p-value "
    "0.000255."
)
table([
    ["Model", "MAE", "RMSE", "MAPE"],
    ["Exponential Smoothing", "11,752.42", "13,071.68", "22.52%"],
    ["ARIMA", "23,717.82", "27,320.37", "53.96%"],
    ["SARIMA", "13,642.80", "15,996.53", "26.61%"],
])
p(
    "Exponential Smoothing had the lowest holdout errors among the three "
    "tested models. Its six-month forecast for January–June 2027 totals "
    "approximately 372,170. These are model forecasts, not guaranteed sales."
)

heading("8. Customer Segmentation")
p(
    "K-Means clustering was applied to 804 customers using total sales, "
    "total profit, total quantity, average discount and number of orders. "
    "Features were standardised before clustering. Four clusters were "
    "selected for business interpretability, although k=2 had the highest "
    "silhouette score among the tested values."
)
table([
    ["Cluster", "Customers", "Avg. Sales", "Avg. Profit", "Interpretation"],
    ["0", "202", "1,551.19", "-96.28", "Lower sales, loss-making"],
    ["1", "264", "3,712.55", "367.00", "Higher volume, profitable"],
    ["2", "55", "9,717.80", "2,281.43", "High-value customers"],
    ["3", "283", "1,761.84", "315.83", "Lower sales, profitable"],
])
p(
    "The first two PCA components explained 73.36% of the variance. "
    "The cluster profiles suggest different retention, cross-selling "
    "and discount-review strategies."
)

heading("9. Machine Learning Results")
table([
    ["Model", "MAE", "RMSE", "R²"],
    ["Linear Regression", "61.709", "214.026", "0.489"],
    ["Decision Tree Regressor", "28.787", "120.929", "0.837"],
])
p(
    "The Decision Tree Regressor performed better than Linear Regression "
    "on the reported test metrics. The leading feature importances were "
    "Sales (0.604) and Discount (0.275). Feature importance indicates "
    "model reliance, not causation."
)
p(
    "The Logistic Regression model classified transactions as above or "
    "below the median profit threshold of 8.69. It achieved accuracy "
    "0.797, precision 0.7911, recall 0.8067, F1-score 0.7988 and "
    "ROC-AUC 0.8833. This is a high-profit classification task, not churn prediction."
)

heading("10. Key Findings and Business Recommendations")
for x in [
    "<b>Review discount practices:</b> Discounted transactions had lower "
    "average profit in this dataset. Evaluate discount levels alongside "
    "product costs and margins.",
    "<b>Retain high-value customers:</b> The high-value cluster had the "
    "highest average sales and profit. Consider loyalty and retention initiatives.",
    "<b>Improve loss-making customer economics:</b> Review discounts, "
    "costs and order composition for the loss-making cluster.",
    "<b>Grow profitable lower-sales customers:</b> Use relevant cross-selling "
    "and bundles to increase order value.",
    "<b>Use forecasts carefully:</b> Exponential Smoothing was the best "
    "of the three tested models on the reported holdout metrics. Monitor "
    "forecast errors as new data arrives.",
    "<b>Monitor performance:</b> Use the dashboard to track sales, profit, "
    "regions, categories and customer segments."
]:
    p("• " + x)

heading("11. Limitations and Future Scope")
p(
    "The analysis is limited to the fields, observations and time period "
    "available in the supplied dataset. Statistical associations do not "
    "prove causation. Forecasts depend on historical patterns and may "
    "change when business conditions change. Clustering results depend "
    "on feature selection and the chosen number of clusters."
)
p(
    "Future work could include more recent data, external business factors, "
    "additional model validation, automated dashboard refreshes, monitoring "
    "of forecast performance and deployment of the analytics workflow."
)

heading("12. Conclusion")
p(
    "The project demonstrates an end-to-end analytics workflow using "
    "data preparation, exploratory analysis, SQL, visualisation, statistical "
    "methods, forecasting, clustering and machine learning. The findings "
    "provide a basis for reviewing discount strategies, understanding "
    "customer groups and monitoring sales performance."
)

# Appendix: include all existing chart files, without guessing their meanings.
chart_files = sorted(glob.glob(os.path.join(CHART_DIR, "chart_*.png")))
if chart_files:
    story.append(PageBreak())
    heading("Appendix: Project Visualisations")
    p(
        "The following figures are included from the existing project chart "
        "exports. Refer to the relevant notebooks for each chart's exact "
        "analysis and interpretation."
    )
    for chart in chart_files:
        name = os.path.basename(chart)
        img = Image(chart, width=6.1*inch, height=3.7*inch)
        img.hAlign = "CENTER"
        story.append(KeepTogether([
            Paragraph(name, styles["Heading3"]),
            img,
            Spacer(1, 12)
        ]))

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("PDF created:", OUT)
print("Charts included:", len(chart_files))
