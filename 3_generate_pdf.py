import pandas as pd
from fpdf import FPDF

# 1. Read cleaned data and calculate summary numbers
df = pd.read_csv("cleaned_telco_churn.csv")
total = len(df)
churned = len(df[df['Churn'] == 'Yes'])
churn_rate = round((churned / total) * 100, 2)
avg_bill = round(df['MonthlyCharges'].mean(), 2)

# 2. Create blank PDF (Page 1: Summary + First 2 Charts)
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", size=16, style="B")
pdf.cell(0, 10, "Telecom Customer Churn Analysis Report", ln=True, align="C")
pdf.ln(5)

# KPI Summary
pdf.set_font("Arial", size=12, style="B")
pdf.cell(0, 8, "1. Executive Summary", ln=True)

pdf.set_font("Arial", size=11)
pdf.cell(0, 7, f"Total Customers: {total}", ln=True)
pdf.cell(0, 7, f"Churned Customers: {churned}", ln=True)
pdf.cell(0, 7, f"Overall Churn Rate: {churn_rate}%", ln=True)
pdf.cell(0, 7, f"Average Monthly Bill: ${avg_bill}", ln=True)
pdf.ln(5)

# Charts 1 & 2
pdf.set_font("Arial", size=12, style="B")
pdf.cell(0, 8, "2. Customer Churn & Contract Analysis", ln=True)
pdf.image("charts/1_churn_count.png", w=120)
pdf.ln(3)
pdf.image("charts/2_contract_churn.png", w=120)

# Page 2: Charts 3 & 4
pdf.add_page()
pdf.image("charts/3_internet_churn.png", w=135)
pdf.ln(8)
pdf.image("charts/4_monthly_charges.png", w=135)

# Page 3: Charts 5 & 6
pdf.add_page()
pdf.image("charts/5_tenure.png", w=135)
pdf.ln(8)
pdf.image("charts/6_payment_bar.png", w=150)

# Page 4: Charts 7 & 8
pdf.add_page()
pdf.image("charts/7_charges_box.png", w=125)
pdf.ln(8)
pdf.image("charts/8_heatmap.png", w=125)

# Page 5: Key Business Recommendations
pdf.add_page()
pdf.set_font("Arial", size=14, style="B")
pdf.cell(0, 10, "3. Key Business Recommendations", ln=True)
pdf.ln(3)

pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 8, "- Convert Month-to-Month Users: Customers on month-to-month plans leave the most. Offer discounts to upgrade them to 1-year or 2-year plans.")
pdf.ln(3)
pdf.multi_cell(0, 8, "- Improve First-Year Support: Most churn happens in the first 12 months. Give new customers onboarding calls and loyalty rewards.")
pdf.ln(3)
pdf.multi_cell(0, 8, "- Review Fiber Optic & Payment Methods: High monthly bills and electronic check payments show higher churn. Offer auto-pay discounts and bundle packages.")

# 3. Save the final PDF
pdf.output("Telecom_Churn_Report.pdf")
print("Success! 'Telecom_Churn_Report.pdf' generated with all 8 charts.")