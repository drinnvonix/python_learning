import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for all charts
sns.set_theme(style="whitegrid")
# Load the sales transaction dataset
df = pd.read_csv("salesDataset.csv")

# Display the first five rows
print("First five rows:")
print(df.head())

# Display dataset shape
print("\nDataset shape:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

# Display dataset information
print("\nDataset information:")
df.info()

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Convert datetime column to datetime
df["datetime"] = pd.to_datetime(df["datetime"])

# Fill missing card values
# Cash transactions do not have a card number
df["card"] = df["card"].fillna("Cash Customer")

# Check missing values again
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Create customer-level data
customer_data = df.groupby("card").agg(
    total_spent=("money", "sum"),
    total_purchases=("money", "count"),
    average_purchase=("money", "mean"),
    unique_products=("coffee_name", "nunique")
).reset_index()

# Display the first five customers
print("\nCustomer-level data:")
print(customer_data.head())

# Display customer dataset shape
print("\nCustomer dataset shape:")
print(customer_data.shape)

# Display customer statistics
print("\nCustomer statistics:")
print(customer_data.describe())

# Find the top 10 customers based on total spending
top_customers = customer_data.sort_values(
    by="total_spent",
    ascending=False
).head(10)

print("\nTop 10 customers by total spending:")
print(top_customers)

# Plot the top 10 customers
plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_customers,
    x="total_spent",
    y="card"
)

plt.title("Top 10 Customers by Total Spending")
plt.xlabel("Total Spending")
plt.ylabel("Customer")

plt.tight_layout()
plt.show()

# Create a histogram showing customer spending
plt.figure(figsize=(10, 6))

sns.histplot(
    data=customer_data,
    x="total_spent",
    bins=30,
    kde=True
)

plt.title("Customer Spending Distribution")
plt.xlabel("Total Spending")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Create a scatter plot between purchases and spending
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=customer_data,
    x="total_purchases",
    y="total_spent"
)

plt.title("Number of Purchases vs Total Spending")
plt.xlabel("Number of Purchases")
plt.ylabel("Total Spending")

plt.tight_layout()
plt.show()

# Create a scatter plot between average purchase and total spending
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=customer_data,
    x="average_purchase",
    y="total_spent"
)

plt.title("Average Purchase vs Total Spending")
plt.xlabel("Average Purchase")
plt.ylabel("Total Spending")

plt.tight_layout()
plt.show()

# Create customer segments using spending percentiles
low_spending = customer_data["total_spent"].quantile(0.25)
high_spending = customer_data["total_spent"].quantile(0.75)

def create_segment(spending):
    if spending <= low_spending:
        return "Low Value"
    elif spending >= high_spending:
        return "High Value"
    else:
        return "Medium Value"

customer_data["segment"] = customer_data[
    "total_spent"
].apply(create_segment)

# Count customers in each segment
segment_counts = customer_data[
    "segment"
].value_counts()

print("\nNumber of customers in each segment:")
print(segment_counts)

# Plot customer segments
plt.figure(figsize=(8, 5))

sns.countplot(
    data=customer_data,
    x="segment"
)

plt.title("Customer Segments")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Calculate statistics for each segment
segment_summary = customer_data.groupby(
    "segment"
).agg(
    customers=("card", "count"),
    average_spending=("total_spent", "mean"),
    average_purchases=("total_purchases", "mean"),
    average_transaction=("average_purchase", "mean"),
    average_unique_products=("unique_products", "mean")
).reset_index()

print("\nCustomer segment summary:")
print(segment_summary)

# Sort segments by average spending
segment_summary = segment_summary.sort_values(
    by="average_spending",
    ascending=False
)

# Plot average spending by segment
plt.figure(figsize=(8, 5))

sns.barplot(
    data=segment_summary,
    x="segment",
    y="average_spending"
)

plt.title("Average Spending by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Average Spending")

plt.tight_layout()
plt.show()

# Import libraries required for K-Means clustering
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Select variables for customer segmentation
features = [
    "total_spent",
    "total_purchases",
    "average_purchase",
    "unique_products"
]

# Create a separate dataset for clustering
X = customer_data[features].copy()

# Scale the data
# Scaling is important because the variables
# have different ranges.
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Create the K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train the model
customer_data["cluster"] = kmeans.fit_predict(
    X_scaled
)

# Display the number of customers in each cluster
print("\nCustomers in each cluster:")
print(customer_data["cluster"].value_counts())

# Calculate average values for each cluster
cluster_summary = customer_data.groupby(
    "cluster"
)[features].mean()

print("\nCluster summary:")
print(cluster_summary)

# Create a scatter plot of the clusters
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=customer_data,
    x="total_purchases",
    y="total_spent",
    hue="cluster",
    palette="deep",
    s=80
)

plt.title("Customer Segmentation Using K-Means")
plt.xlabel("Number of Purchases")
plt.ylabel("Total Spending")

plt.legend(title="Cluster")
plt.tight_layout()
plt.show()

# Create a second visualization using average purchase
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=customer_data,
    x="average_purchase",
    y="total_spent",
    hue="cluster",
    palette="deep",
    s=80
)

plt.title("Customer Clusters: Average Purchase vs Total Spending")
plt.xlabel("Average Purchase")
plt.ylabel("Total Spending")

plt.legend(title="Cluster")
plt.tight_layout()
plt.show()

# Save the customer segmentation results
output_file = "customer_segmentation_results.csv"

customer_data.to_csv(
    output_file,
    index=False
)

print("\nCustomer segmentation results saved to:")
print(output_file)

print("\nCustomer segmentation analysis completed.")