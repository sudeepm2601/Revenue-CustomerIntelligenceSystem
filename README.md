# Revenue & Customer Intelligence System

An end-to-end data analytics project that analyzes retail transaction data to uncover revenue trends, customer behavior, product performance, and country-wise sales patterns.

The project uses Python for data cleaning and analysis and Power BI for interactive business intelligence and dashboard reporting.

---

## 📌 Project Overview

The objective of this project is to transform raw retail transaction data into meaningful business insights that can help organizations understand:

- Overall revenue performance
- Monthly sales trends
- Product demand and revenue contribution
- Country-wise revenue performance
- High-value customers
- Average Order Value
- Customer purchasing behavior

The project follows a complete data analytics workflow:

**Raw Data → Data Cleaning → Feature Engineering → EDA → KPI Analysis → Power BI Dashboard → Business Insights**

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas**
- **Power BI**
- **Jupyter Notebook / VS Code**
- **CSV**

---

## 📂 Dataset

The project uses an online retail transaction dataset containing information such as:

- Invoice
- StockCode
- Description
- Quantity
- InvoiceDate
- Price
- Customer ID
- Country

The dataset contains **1M+ transaction records** from an online retail business.

---

## 🧹 Data Cleaning

The raw dataset was cleaned and prepared for analysis using Pandas.

Key data-cleaning steps included:

- Checked the dataset structure and data types.
- Identified and handled missing values.
- Removed records with missing product descriptions where appropriate.
- Investigated missing Customer IDs.
- Identified duplicate records.
- Examined negative quantities representing returned/cancelled products.
- Investigated transactions with zero prices.
- Converted `InvoiceDate` from object to datetime format.
- Converted `Customer ID` to an appropriate data type.
- Created a cleaned dataset for Power BI analysis.

---

## ⚙️ Feature Engineering

New analytical fields and business metrics were created to support analysis.

### Revenue

```text
Revenue = Quantity × Price