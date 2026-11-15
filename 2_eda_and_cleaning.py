import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a folder to save chart images
os.makedirs("charts", exist_ok=True)

# 1. Load the dataset
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

# 2. Clean the data
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# 3. Save clean file (for Power BI and PDF)
df.to_csv("cleaned_telco_churn.csv", index=False)
print("Data cleaned! Total rows:", len(df))

# ==========================================
# SIMPLE CHARTS (5 MAIN VISUALIZATIONS)
# ==========================================

# Chart 1: Churn Count (Bar Chart)
sns.countplot(data=df, x='Churn')
plt.title("1. Customer Churn Count")
plt.savefig("charts/1_churn_count.png")
plt.clf() # Clears the screen for the next chart

# Chart 2: Churn by Contract Type
sns.countplot(data=df, x='Contract', hue='Churn')
plt.title("2. Churn by Contract Type")
plt.savefig("charts/2_contract_churn.png")
plt.clf()

# Chart 3: Churn by Internet Service
sns.countplot(data=df, x='InternetService', hue='Churn')
plt.title("3. Churn by Internet Service")
plt.savefig("charts/3_internet_churn.png")
plt.clf()

# Chart 4: Monthly Charges Distribution
sns.histplot(data=df, x='MonthlyCharges', hue='Churn')
plt.title("4. Monthly Charges Distribution")
plt.savefig("charts/4_monthly_charges.png")
plt.clf()

# Chart 5: Customer Tenure (Months) Distribution
sns.histplot(data=df, x='tenure', hue='Churn')
plt.title("5. Customer Tenure Distribution")
plt.savefig("charts/5_tenure.png")
plt.clf()

# Chart 6: Churn by Payment Method
plt.figure(figsize=(8, 4))
sns.countplot(data=df, y='PaymentMethod', hue='Churn', palette=['#4CAF50', '#F44336'])
plt.title("6. Churn by Payment Method")
plt.savefig("charts/6_payment_bar.png", bbox_inches='tight', dpi=150)
plt.close()

# Chart 7: Monthly Charges Box Plot
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='Churn', y='MonthlyCharges', palette=['#4CAF50', '#F44336'])
plt.title("7. Monthly Charges Box Plot")
plt.savefig("charts/7_charges_box.png", bbox_inches='tight', dpi=150)
plt.close()

# Chart 8: Correlation Heatmap
plt.figure(figsize=(6, 5))
numeric_data = df[['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']]
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("8. Correlation Heatmap")
plt.savefig("charts/8_heatmap.png", bbox_inches='tight', dpi=150)
plt.close()

print("All 8 charts saved inside the 'charts/' folder!")