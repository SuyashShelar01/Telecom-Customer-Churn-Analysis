# Telecom Customer Churn Analysis (End-to-End Data Analytics Project)

![Dashboard Preview](dashboard_preview.png)

## 📌 Project Overview
An end-to-end data analysis project analyzing customer churn across **7,043 telecom customer records**[cite: 15]. The workflow covers database management in **MySQL**, data cleaning and exploratory data analysis (EDA) in **Python**, automated PDF reporting with **FPDF**, and interactive business intelligence dashboarding in **Power BI**[cite: 15].

## 🛠️ Tech Stack
* **Database:** MySQL (`LOAD DATA LOCAL INFILE`, `GROUP BY`, aggregations)
* **Programming & EDA:** Python (`Pandas`, `Matplotlib`, `Seaborn`)
* **Automated Reporting:** `fpdf2` (compiles KPIs, 8 charts, and business recommendations into a multi-page PDF)
* **Visualization:** Power BI Desktop (DAX measures, interactive slicers, KPI cards)[cite: 15]

## 📊 Key Findings & Business Insights
* **Overall Churn:** **2,287** out of **7,043** customers churned (**32.47%** churn rate)[cite: 15], resulting in **$137.62K** in monthly recurring revenue lost[cite: 15].
* **Contract Type:** **Month-to-month** contracts account for the highest volume of churn compared to One-year and Two-year contracts[cite: 15].
* **Internet Service:** **Fiber optic** subscribers show significantly higher churn than DSL or no-internet users[cite: 15].
* **Payment Method:** Customers paying via **Electronic check** have the highest churn rate among all payment methods[cite: 15].

## 💡 Strategic Recommendations
1. **Contract Migration:** Offer targeted discounts or loyalty perks to convert Month-to-Month customers into 1-year or 2-year plans.
2. **Early Onboarding Support:** Strengthen customer support and check-ins during the first 12 months of tenure.
3. **Billing & Service Review:** Audit Fiber Optic pricing/service quality and incentivize automatic payment methods (Bank Transfer / Credit Card) to reduce payment-related churn.

## 📁 Project Structure
* `sql_queries.sql` — Database schema, bulk CSV import, and business SQL queries.
* `2_eda_and_cleaning.py` — Data cleaning script (`cleaned_telco_churn.csv`) and 8 EDA visualizations (`charts/`).
* `3_generate_pdf.py` — Automated script generating `Telecom_Churn_Report.pdf`.
* `Telecom_Churn_Dashboard.pbix` — Interactive Power BI dashboard[cite: 15].
* `dashboard_preview.png` — Dashboard visual preview[cite: 15].