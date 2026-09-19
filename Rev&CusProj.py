import pandas as pd 
import os
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\Sudeep M\Desktop\Revenue & Customer Behaviour Intelligence System\online_retail.csv.zip")



df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])
print("First five rows")

#print(df.head())


print("Last five rows")
#print(df.tail())

#Number of rows and columns 

print("Number of rows and colums")
print(df.shape)

print(df.columns)

print(df.dtypes)

df.info()

print(df.describe())

print(df.describe(include='object'))

print(df.isnull().sum())

print(df.duplicated().sum())

print(df.nunique())

print(df[df['Price']<0])
print(df[df['Quantity']<0])


# seperate dataframe
sales_df=df[df['Quantity']>0]

#print(sales_df)

return_df=df[df['Quantity']<0]

bad_data_df=df[df['Description']=='Adjust bad debt']

print(bad_data_df)

print(df.isnull().sum())

print(df[df['Description'].isnull()].head(20))

print(df[df['Customer ID'].isnull()].head(20))

# print(df[df['Description'].isnull()]['StockCode'].value_counts())

#print(df[df['Description'].isnull()][['StockCode', 'Quantity', 'Price']].head(20))

df=df[df['Description'].notna()]

print(df.isnull().sum())

print(df.duplicated().sum())

dup=df[df.duplicated()]
print(dup.head(20))
print(df.shape)
df.drop_duplicates(inplace=True)

df.info()
print("Duplicates are : ")
print(df.duplicated().sum())

print(df.shape)

#df['Customer ID']=df['Customer ID'].astype(str)

df.info()

# Freature Engineering 

df['Revenue']=df['Quantity']*df['Price']

df['Year']=df['InvoiceDate'].dt.year

df['Month']=df['InvoiceDate'].dt.month

df['Month_Name']=df['InvoiceDate'].dt.month_name()

df['Quarter']=df['InvoiceDate'].dt.quarter

df['Day']=df['InvoiceDate'].dt.day_name()

df['Hour']=df['InvoiceDate'].dt.hour

print(df.head())

print(df.columns)

# Exploratory Data Analysis

total_revenue=df['Revenue'].sum()

print(f"Total Revenue is : {total_revenue}")

total_orders=df['Invoice'].nunique()
print(f"total orders is : {total_orders}")

total_customers=df['Customer ID'].nunique()
print(f"Total Customers are : {total_customers}")

total_products=df['Description'].nunique()
print(f"Total Products are : {total_products}")

average_order_value=total_revenue/total_orders

print(f"Average Order by Value is : {average_order_value}")

# Sales Analysis

monthly_revenue=(
    df.groupby(['Month','Month_Name'])['Revenue']
      .sum()
      .reset_index()
      .sort_values('Month')
)

print(monthly_revenue)

# top 10 products 

top_products=(
    df.groupby('Description')['Revenue']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_products)


customer_df = df[df['Customer ID'].notna()]

# top 10 customers

top_customers=(
    customer_df.groupby('Customer ID')['Revenue']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_customers)

country_revenue = (
    df.groupby('Country')['Revenue']
      .sum()
      .sort_values(ascending=False)
)

print(country_revenue)



top_quantity = (
    df.groupby('Description')['Quantity']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_quantity)

yearly_revenue = (
    df.groupby('Year')['Revenue']
      .sum()
      .sort_values()
)

print(yearly_revenue)

quarter_revenue = (
    df.groupby('Quarter')['Revenue']
      .sum()
      .sort_values()
)

print(quarter_revenue)

day_revenue = (
    df.groupby('Day')['Revenue']
      .sum()
      .sort_values()
)
print(day_revenue)

hour_revenue = (
    df.groupby('Hour')['Revenue']
      .sum()
)

print(hour_revenue)

top_quantity = (
    df.groupby('Description')['Quantity']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_quantity)

customer_orders = (
    customer_df.groupby('Customer ID')['Invoice']
               .nunique()
               .sort_values(ascending=False)
)

print(customer_orders.head(10))

country_orders = (
    df.groupby('Country')['Invoice']
      .nunique()
      .sort_values(ascending=False)
)

print(country_orders)

df.to_csv(r"C:\Users\Sudeep M\Desktop\Revenue&CustomerIntelligenceSystem\Cleaned_Data.csv",index=False)

print("Cleaned data saved successfully!")

print("Current wprking directory ")
print(os.getcwd())