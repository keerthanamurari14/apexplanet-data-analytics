import pandas as pd
from pathlib import Path
from datetime import datetime
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "data/processed/superstore_cleaned.csv"
OUTPUT = ROOT / "reports"

def format_sheet(ws, currency_columns=None):
    currency_columns = currency_columns or []
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions

    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF", size=11)
        cell.fill = PatternFill("solid", fgColor="1F4E78")
        cell.alignment = Alignment(horizontal="center")

    for column in ws.columns:
        letter = get_column_letter(column[0].column)
        width = max(len(str(cell.value or "")) for cell in column) + 4
        ws.column_dimensions[letter].width = min(max(width, 15), 35)

    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(vertical="center")
            if cell.column in currency_columns:
                cell.number_format = '"₹"#,##0.00'

def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(INPUT)
    df.columns = df.columns.str.strip().str.lower()
    df = df.drop_duplicates()

    for col in ["sales", "profit", "quantity", "discount"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    kpis = [
        ("Generated At", datetime.now().strftime("%d-%m-%Y %H:%M")),
        ("Total Records", len(df)),
        ("Total Orders", df["order_id"].nunique()),
        ("Total Customers", df["customer_id"].nunique()),
        ("Total Sales (₹)", df["sales"].sum()),
        ("Total Profit (₹)", df["profit"].sum()),
        ("Total Quantity", df["quantity"].sum()),
        ("Average Discount", df["discount"].mean()),
        ("Average Sales (₹)", df["sales"].mean()),
        ("Average Profit (₹)", df["profit"].mean()),
        ("Missing Values", int(df.isna().sum().sum()))
    ]

    summary = pd.DataFrame(kpis, columns=["KPI", "Value"])
    category = df.groupby("category", as_index=False).agg(
        Total_Sales=("sales", "sum"),
        Total_Profit=("profit", "sum"),
        Total_Quantity=("quantity", "sum")
    )
    region = df.groupby("region", as_index=False).agg(
        Total_Sales=("sales", "sum"),
        Total_Profit=("profit", "sum")
    )

    with pd.ExcelWriter(OUTPUT / "automation_summary.xlsx", engine="openpyxl") as writer:
        summary.to_excel(writer, sheet_name="KPI Summary", index=False)
        category.to_excel(writer, sheet_name="Category Analysis", index=False)
        region.to_excel(writer, sheet_name="Region Analysis", index=False)

        workbook = writer.book
        format_sheet(workbook["KPI Summary"])
        format_sheet(workbook["Category Analysis"], [2, 3])
        format_sheet(workbook["Region Analysis"], [2, 3])

    summary.to_csv(OUTPUT / "automation_kpis.csv", index=False)
    print("SUCCESS: Formatted reports generated!")
    print(summary.to_string(index=False))
    print("Excel: reports/automation_summary.xlsx")
    print("CSV: reports/automation_kpis.csv")

if __name__ == "__main__":
    main()
