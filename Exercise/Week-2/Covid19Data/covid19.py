import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for all charts
sns.set_theme(style="whitegrid")

# Load the country-level COVID dataset
covid_country = pd.read_csv("covid19Dataset.csv")

# Display the first five rows
print("First five rows:")
print(covid_country.head())

# Display the number of rows and columns
print("\nDataset shape:")
print(covid_country.shape)

# Display column names
print("\nColumn names:")
print(covid_country.columns.tolist())

# Display information about the dataset
print("\nDataset information:")
covid_country.info()

# Display statistical summary
print("\nStatistical summary:")
print(covid_country.describe())

# Check for missing values
print("\nMissing values:")
print(covid_country.isnull().sum())

# Check for duplicate rows
print("\nNumber of duplicate rows:")
print(covid_country.duplicated().sum())

# Remove unnecessary spaces from column names
covid_country.columns = covid_country.columns.str.strip()

# Check the top 10 countries based on confirmed cases
top_confirmed = covid_country.sort_values(
    by="Confirmed",
    ascending=False
).head(10)

print("\nTop 10 countries by confirmed cases:")
print(
    top_confirmed[
        ["Country/Region", "Confirmed", "Deaths", "Recovered"]
    ]
)

# Create a bar chart for the top 10 countries by confirmed cases
plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_confirmed,
    x="Confirmed",
    y="Country/Region"
)

plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.xlabel("Confirmed Cases")
plt.ylabel("Country")

plt.tight_layout()
plt.show()

# Find the top 10 countries based on deaths
top_deaths = covid_country.sort_values(
    by="Deaths",
    ascending=False
).head(10)

print("\nTop 10 countries by deaths:")
print(
    top_deaths[
        ["Country/Region", "Confirmed", "Deaths"]
    ]
)

# Create a bar chart for deaths
plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_deaths,
    x="Deaths",
    y="Country/Region"
)

plt.title("Top 10 Countries by COVID-19 Deaths")
plt.xlabel("Deaths")
plt.ylabel("Country")

plt.tight_layout()
plt.show()

# Find the top 10 countries based on recovered cases
top_recovered = covid_country.sort_values(
    by="Recovered",
    ascending=False
).head(10)

print("\nTop 10 countries by recovered cases:")
print(
    top_recovered[
        ["Country/Region", "Confirmed", "Deaths", "Recovered"]
    ]
)

# Create a bar chart for recovered cases
plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_recovered,
    x="Recovered",
    y="Country/Region"
)

plt.title("Top 10 Countries by Recovered COVID-19 Cases")
plt.xlabel("Recovered Cases")
plt.ylabel("Country")

plt.tight_layout()
plt.show()

# Calculate total confirmed cases by WHO region
region_cases = covid_country.groupby(
    "WHO Region"
)["Confirmed"].sum().sort_values(
    ascending=False
)

print("\nConfirmed cases by WHO region:")
print(region_cases)

# Create a chart for WHO regions
plt.figure(figsize=(10, 6))

region_cases.plot(kind="bar")

plt.title("Confirmed COVID-19 Cases by WHO Region")
plt.xlabel("WHO Region")
plt.ylabel("Confirmed Cases")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate total deaths by WHO region
region_deaths = covid_country.groupby(
    "WHO Region"
)["Deaths"].sum().sort_values(
    ascending=False
)

print("\nDeaths by WHO region:")
print(region_deaths)

# Create a chart for deaths by WHO region
plt.figure(figsize=(10, 6))

region_deaths.plot(kind="bar")

plt.title("COVID-19 Deaths by WHO Region")
plt.xlabel("WHO Region")
plt.ylabel("Deaths")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Find countries with the highest death rate
top_death_rate = covid_country.sort_values(
    by="Deaths / 100 Cases",
    ascending=False
).head(10)

print("\nTop 10 countries by death rate:")
print(
    top_death_rate[
        [
            "Country/Region",
            "Confirmed",
            "Deaths",
            "Deaths / 100 Cases"
        ]
    ]
)

# Create a chart for death rate
plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_death_rate,
    x="Deaths / 100 Cases",
    y="Country/Region"
)

plt.title("Top 10 Countries by COVID-19 Death Rate")
plt.xlabel("Deaths per 100 Confirmed Cases")
plt.ylabel("Country")

plt.tight_layout()
plt.show()

print("\nLoading historical COVID time-series data...")

covid_time = pd.read_csv("owid-covid-data.csv")

print("\nHistorical COVID data loaded successfully.")

print("\nTime-series dataset shape:")
print(covid_time.shape)

print("\nTime-series columns:")
print(covid_time.columns.tolist())

# Convert date column to datetime
covid_time["date"] = pd.to_datetime(
    covid_time["date"]
)

# Select India from the dataset
india_covid = covid_time[
    covid_time["location"] == "India"
].copy()

# Remove rows where total cases are missing
india_covid = india_covid.dropna(
    subset=["total_cases"]
)

# Sort data by date
india_covid = india_covid.sort_values(
    by="date"
)

print("\nIndia COVID data:")
print(
    india_covid[
        ["date", "total_cases"]
    ].tail()
)

# Plot total confirmed cases in India
plt.figure(figsize=(14, 6))

plt.plot(
    india_covid["date"],
    india_covid["total_cases"]
)

plt.title("COVID-19 Confirmed Cases in India Over Time")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Remove rows where total deaths are missing
india_deaths = india_covid.dropna(
    subset=["total_deaths"]
)

# Plot total deaths in India
plt.figure(figsize=(14, 6))

plt.plot(
    india_deaths["date"],
    india_deaths["total_deaths"]
)

plt.title("COVID-19 Deaths in India Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Calculate daily new cases
india_covid["new_cases"] = india_covid[
    "total_cases"
].diff()

# Replace negative values with zero
india_covid["new_cases"] = india_covid[
    "new_cases"
].clip(lower=0)

# Plot daily new cases
plt.figure(figsize=(14, 6))

plt.plot(
    india_covid["date"],
    india_covid["new_cases"]
)

plt.title("Daily New COVID-19 Cases in India")
plt.xlabel("Date")
plt.ylabel("New Cases")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Calculate 7-day moving average
india_covid["7_day_average"] = india_covid[
    "new_cases"
].rolling(window=7).mean()

# Plot daily cases and moving average
plt.figure(figsize=(14, 6))

plt.plot(
    india_covid["date"],
    india_covid["new_cases"],
    alpha=0.4,
    label="Daily New Cases"
)

plt.plot(
    india_covid["date"],
    india_covid["7_day_average"],
    linewidth=2,
    label="7-Day Moving Average"
)

plt.title("COVID-19 Cases in India with 7-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Cases")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Compare COVID-19 cases between India, United States and Brazil
selected_countries = [
    "India",
    "United States",
    "Brazil"
]

comparison = covid_time[
    covid_time["location"].isin(selected_countries)
].copy()

comparison = comparison.dropna(
    subset=["total_cases"]
)

# Create country comparison chart
plt.figure(figsize=(14, 6))

for country in selected_countries:
    country_data = comparison[
        comparison["location"] == country
    ]

    plt.plot(
        country_data["date"],
        country_data["total_cases"],
        label=country
    )

plt.title("COVID-19 Confirmed Cases Comparison")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

print("\nCOVID-19 analysis completed.")