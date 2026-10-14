import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("retail_sales.csv")

# Display original data
print("RETAIL SALES DATA ANALYSIS")
print("=" * 40)

print("\nOriginal Dataset:")
print(df.to_string(index=False))

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing values
df = df.dropna()

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df.to_string(index=False))

# Calculate total revenue
total_revenue = df["Total_Sales"].sum()

# Calculate total quantity sold
total_quantity = df["Quantity"].sum()

# Calculate average sales
average_sales = df["Total_Sales"].mean()

# Find best-selling product by quantity
product_sales = df.groupby("Product")["Quantity"].sum()
best_selling_product = product_sales.idxmax()

# Calculate sales by category
category_sales = df.groupby("Category")["Total_Sales"].sum()

# Display results
print("\nSALES SUMMARY")
print("=" * 40)
print(f"Total Revenue: Rs. {total_revenue:,.2f}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Transaction Sales: Rs. {average_sales:,.2f}")
print(f"Best-Selling Product: {best_selling_product}")

print("\nRevenue by Category:")
print(category_sales.to_string())

# Plot 1: Revenue by category
plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Plot 2: Quantity sold by product
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 3: Daily sales trend
df["Date"] = pd.to_datetime(df["Date"])
daily_sales = df.groupby("Date")["Total_Sales"].sum()

plt.figure(figsize=(10, 5))
daily_sales.plot(kind="line", marker="o")
plt.title("Daily Retail Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save the analyzed dataset
df.to_csv("analyzed_retail_sales.csv", index=False)

print("\nAnalyzed data saved to analyzed_retail_sales.csv")
print("\nProject completed successfully!")
