import pandas as pd

# Reading the first CSV file and pivoting the DataFrame to set 'date' as index, 'city' as columns, and 'humidity' as values
df = pd.read_csv("Excels\\weather5.csv")
df = df.pivot(index="date", columns="city", values="humidity")  # Index represents rows, displaying only humidity values
print(df)

# ----------Another csv File--------------#

# Reading the second CSV file containing the same date
df = pd.read_csv("Excels\\weather6.csv")

# Pivoting the DataFrame to set 'city' as index, 'date' as columns, and averaging values for same dates
# By default, aggfunc= is mean, you can add margin=True to include an "All" column with the aggregation result
df = df.pivot_table(index="city", columns="date")
print(df)

# ------------Another CSV File-------------#

# Reading the third CSV file and converting the 'date' column to datetime format
df = pd.read_csv("Excels\\weather7.csv")
df["date"] = pd.to_datetime(df["date"])

# Pivoting the DataFrame to group by month and set 'city' as columns, averaging values for each month
df = df.pivot_table(index=pd.Grouper(freq='M', key="date"), columns="city")  # Averages data for the whole month
print(df)
