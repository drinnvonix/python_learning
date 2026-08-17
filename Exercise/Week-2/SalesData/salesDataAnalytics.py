# SALES DATA ANALYSIS

# This project analyzes coffee shop sales data.
# We will clean the data, perform sales analysis,
# create visualizations and build an interactive dashboard.


# 1. IMPORT LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from dash import Dash, html, dcc

sns.set_theme(style="whitegrid")


# 2. LOAD THE DATASET

df = pd.read_csv("salesDataset.csv")

print("First 5 Rows:")
print(df.head())
print()

print("Dataset Shape:")
print(df.shape)
print()

print("Dataset Information:")
df.info()
print()

print("Descriptive Statistics:")
print(df.describe())
print()

print("Column Names:")
print(df.columns.tolist())
print()


# 3. CHECK FOR MISSING VALUES

print("Missing Values Before Cleaning:")
print(df.isnull().sum())
print()

# Missing card values are treated as cash customers.
df["card"] = df["card"].fillna("Cash Customer")

print("Missing Values After Cleaning:")
print(df.isnull().sum())
print()


# 4. CHECK FOR DUPLICATES

duplicate_count = df.duplicated().sum()

print("Number of Duplicate Rows:", duplicate_count)
print()


# 5. CONVERT DATE AND TIME COLUMNS

df["date"] = pd.to_datetime(df["date"])
df["datetime"] = pd.to_datetime(df["datetime"])

print("Updated Data Types:")
print(df.dtypes)
print()


# 6. CREATE DATE AND TIME FEATURES

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["month_name"] = df["date"].dt.month_name()
df["day_name"] = df["date"].dt.day_name()
df["hour"] = df["datetime"].dt.hour

print("Dataset After Feature Creation:")
print(df.head())
print()


# 7. BASIC SALES KPIs

total_sales = df["money"].sum()
average_sale = df["money"].mean()
total_transactions = len(df)
total_customers = df["card"].nunique()

print("KEY SALES METRICS")
print(f"Total Revenue:        {total_sales:.2f}")
print(f"Average Transaction:  {average_sale:.2f}")
print(f"Total Transactions:   {total_transactions}")
print(f"Unique Customers:     {total_customers}")
print()


# 8. SALES BY COFFEE TYPE

coffee_sales = (
    df.groupby("coffee_name")["money"]
    .sum()
    .sort_values(ascending=False)
)

coffee_count = df["coffee_name"].value_counts()

print("Revenue by Coffee Type:")
print(coffee_sales)
print()

print("Number of Transactions by Coffee Type:")
print(coffee_count)
print()


# 9. TRANSACTIONS BY COFFEE

plt.figure(figsize=(10, 6))

coffee_count.sort_values().plot(
    kind="barh",
    edgecolor="black"
)

plt.title("Number of Transactions by Coffee Type", fontsize=16)
plt.xlabel("Number of Transactions")
plt.ylabel("Coffee Type")
plt.tight_layout()
plt.show()


# 10. REVENUE BY COFFEE

plt.figure(figsize=(10, 6))

coffee_sales.sort_values().plot(
    kind="barh",
    edgecolor="black"
)

plt.title("Revenue by Coffee Type", fontsize=16)
plt.xlabel("Revenue")
plt.ylabel("Coffee Type")
plt.tight_layout()
plt.show()


# 11. PAYMENT METHOD ANALYSIS

payment_sales = df.groupby("cash_type")["money"].sum()
payment_count = df["cash_type"].value_counts()

print("Revenue by Payment Method:")
print(payment_sales)
print()

print("Number of Transactions by Payment Method:")
print(payment_count)
print()


# 12. REVENUE BY PAYMENT METHOD

plt.figure(figsize=(8, 5))

ax = payment_sales.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Revenue by Payment Method", fontsize=16)
plt.xlabel("Payment Method")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f", padding=3)

plt.tight_layout()
plt.show()


# 13. TRANSACTIONS BY PAYMENT METHOD

plt.figure(figsize=(8, 5))

ax = payment_count.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Number of Transactions by Payment Method", fontsize=16)
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=0)

for container in ax.containers:
    ax.bar_label(container, padding=3)

plt.tight_layout()
plt.show()


# 14. MONTHLY SALES TREND

monthly_sales = df.groupby(
    df["date"].dt.to_period("M")
)["money"].sum()

print("Monthly Sales:")
print(monthly_sales)
print()


# 15. MONTHLY SALES VISUALIZATION

plt.figure(figsize=(14, 6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


# 16. SALES BY HOUR

hourly_sales = df.groupby("hour")["money"].sum()

print("Sales by Hour:")
print(hourly_sales)
print()


# 17. SALES BY HOUR VISUALIZATION

plt.figure(figsize=(10, 5))

plt.plot(
    hourly_sales.index,
    hourly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Sales by Hour of the Day", fontsize=16)
plt.xlabel("Hour of Day")
plt.ylabel("Revenue")
plt.xticks(hourly_sales.index)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


# 18. SALES BY DAY OF THE WEEK

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

daily_sales = (
    df.groupby("day_name")["money"]
    .sum()
    .reindex(day_order)
)

print("Sales by Day of the Week:")
print(daily_sales)
print()


# 19. SALES BY DAY VISUALIZATION

plt.figure(figsize=(10, 5))

ax = daily_sales.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Sales by Day of the Week", fontsize=16)
plt.xlabel("Day")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

for container in ax.containers:
    ax.bar_label(container, fmt="%.0f", padding=3)

plt.tight_layout()
plt.show()


# 20. TOP COFFEE ANALYSIS

top_coffee = coffee_sales.idxmax()
top_coffee_revenue = coffee_sales.max()

most_sold_coffee = coffee_count.idxmax()
most_sold_count = coffee_count.max()

print("Top Coffee by Revenue:")
print(f"{top_coffee} - {top_coffee_revenue:.2f}")
print()

print("Most Frequently Sold Coffee:")
print(f"{most_sold_coffee} - {most_sold_count} transactions")
print()


# 21. FINAL SALES SUMMARY

print("FINAL SALES SUMMARY")
print(f"Total Revenue:          {total_sales:.2f}")
print(f"Average Transaction:    {average_sale:.2f}")
print(f"Total Transactions:     {total_transactions}")
print(f"Unique Customers:       {total_customers}")
print(f"Top Coffee by Revenue:  {top_coffee}")
print(f"Top Coffee Revenue:     {top_coffee_revenue:.2f}")
print(f"Most Sold Coffee:       {most_sold_coffee}")
print(f"Most Sold Transactions: {most_sold_count}")
print(f"Best Payment Method:    {payment_sales.idxmax()}")
print(f"Best Sales Day:         {daily_sales.idxmax()}")
print(f"Best Sales Hour:        {hourly_sales.idxmax()}")
print()


# 22. CREATE INTERACTIVE SALES DASHBOARD

# The dashboard contains four KPIs and six charts.


# 22.1 PREPARE DASHBOARD DATA

coffee_revenue = (
    df.groupby("coffee_name", as_index=False)["money"]
    .sum()
    .sort_values("money", ascending=False)
)

coffee_transactions = (
    df.groupby("coffee_name")
    .size()
    .reset_index(name="transactions")
    .sort_values("transactions", ascending=False)
)

monthly_revenue = (
    df.groupby(df["date"].dt.to_period("M"))["money"]
    .sum()
    .reset_index()
)

monthly_revenue["date"] = monthly_revenue["date"].astype(str)

payment_revenue = (
    df.groupby("cash_type", as_index=False)["money"]
    .sum()
    .sort_values("money", ascending=False)
)

daily_revenue = (
    df.groupby("day_name")["money"]
    .sum()
    .reindex(day_order)
    .reset_index()
)

hourly_revenue = (
    df.groupby("hour")["money"]
    .sum()
    .reset_index()
)


# 22.2 CREATE PLOTLY CHARTS

fig_coffee_revenue = px.bar(
    coffee_revenue,
    x="money",
    y="coffee_name",
    orientation="h",
    title="Revenue by Coffee",
    labels={
        "money": "Revenue",
        "coffee_name": "Coffee"
    },
    text="money"
)

fig_coffee_revenue.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig_coffee_revenue.update_layout(
    yaxis={"categoryorder": "total ascending"}
)


fig_coffee_transactions = px.bar(
    coffee_transactions,
    x="transactions",
    y="coffee_name",
    orientation="h",
    title="Transactions by Coffee",
    labels={
        "transactions": "Transactions",
        "coffee_name": "Coffee"
    },
    text="transactions"
)

fig_coffee_transactions.update_traces(
    textposition="outside"
)

fig_coffee_transactions.update_layout(
    yaxis={"categoryorder": "total ascending"}
)


fig_monthly_revenue = px.line(
    monthly_revenue,
    x="date",
    y="money",
    title="Monthly Revenue",
    labels={
        "date": "Month",
        "money": "Revenue"
    },
    markers=True
)

fig_monthly_revenue.update_layout(
    xaxis=dict(tickangle=-45)
)


fig_payment_revenue = px.pie(
    payment_revenue,
    names="cash_type",
    values="money",
    title="Revenue by Payment Method",
    hole=0.4
)

fig_payment_revenue.update_traces(
    textposition="inside",
    textinfo="percent+label"
)


fig_daily_revenue = px.bar(
    daily_revenue,
    x="day_name",
    y="money",
    title="Sales by Day",
    labels={
        "day_name": "Day",
        "money": "Revenue"
    },
    text="money"
)

fig_daily_revenue.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig_daily_revenue.update_layout(
    xaxis={
        "categoryorder": "array",
        "categoryarray": day_order
    }
)


fig_hourly_revenue = px.line(
    hourly_revenue,
    x="hour",
    y="money",
    title="Sales by Hour",
    labels={
        "hour": "Hour of Day",
        "money": "Revenue"
    },
    markers=True
)

fig_hourly_revenue.update_layout(
    xaxis=dict(dtick=1)
)


# 22.3 CREATE DASH APPLICATION

app = Dash(__name__)


# 22.4 CREATE DASHBOARD LAYOUT

app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f5f6fa",
        "padding": "20px"
    },
    children=[
        html.H1(
            "Coffee Shop Sales Dashboard",
            style={
                "textAlign": "center",
                "marginBottom": "30px"
            }
        ),

        # KPI cards
        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)",
                "gap": "20px",
                "marginBottom": "30px"
            },
            children=[
                html.Div(
                    [
                        html.H4("Total Revenue"),
                        html.H2(f"{total_sales:,.2f}")
                    ],
                    style={
                        "backgroundColor": "white",
                        "padding": "20px",
                        "borderRadius": "10px",
                        "textAlign": "center"
                    }
                ),

                html.Div(
                    [
                        html.H4("Total Transactions"),
                        html.H2(f"{total_transactions:,}")
                    ],
                    style={
                        "backgroundColor": "white",
                        "padding": "20px",
                        "borderRadius": "10px",
                        "textAlign": "center"
                    }
                ),

                html.Div(
                    [
                        html.H4("Average Transaction"),
                        html.H2(f"{average_sale:,.2f}")
                    ],
                    style={
                        "backgroundColor": "white",
                        "padding": "20px",
                        "borderRadius": "10px",
                        "textAlign": "center"
                    }
                ),

                html.Div(
                    [
                        html.H4("Unique Customers"),
                        html.H2(f"{total_customers:,}")
                    ],
                    style={
                        "backgroundColor": "white",
                        "padding": "20px",
                        "borderRadius": "10px",
                        "textAlign": "center"
                    }
                )
            ]
        ),

        # First row
        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "1fr 1fr",
                "gap": "20px",
                "marginBottom": "20px"
            },
            children=[
                html.Div(
                    dcc.Graph(figure=fig_coffee_revenue),
                    style={
                        "backgroundColor": "white",
                        "borderRadius": "10px"
                    }
                ),

                html.Div(
                    dcc.Graph(figure=fig_coffee_transactions),
                    style={
                        "backgroundColor": "white",
                        "borderRadius": "10px"
                    }
                )
            ]
        ),

        # Second row
        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "1fr 1fr",
                "gap": "20px",
                "marginBottom": "20px"
            },
            children=[
                html.Div(
                    dcc.Graph(figure=fig_monthly_revenue),
                    style={
                        "backgroundColor": "white",
                        "borderRadius": "10px"
                    }
                ),

                html.Div(
                    dcc.Graph(figure=fig_payment_revenue),
                    style={
                        "backgroundColor": "white",
                        "borderRadius": "10px"
                    }
                )
            ]
        ),

        # Third row
        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "1fr 1fr",
                "gap": "20px"
            },
            children=[
                html.Div(
                    dcc.Graph(figure=fig_daily_revenue),
                    style={
                        "backgroundColor": "white",
                        "borderRadius": "10px"
                    }
                ),

                html.Div(
                    dcc.Graph(figure=fig_hourly_revenue),
                    style={
                        "backgroundColor": "white",
                        "borderRadius": "10px"
                    }
                )
            ]
        )
    ]
)


# 22.5 RUN THE DASHBOARD

if __name__ == "__main__":
    app.run(debug=True)