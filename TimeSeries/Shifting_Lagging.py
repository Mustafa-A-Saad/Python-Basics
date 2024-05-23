import pandas as pd

# Read CSV file into DataFrame, parsing 'Date' column as dates and setting it as index
df = pd.read_csv('Excels\\fb.csv', parse_dates=['Date'], index_col=['Date'])
print(df)

# Shift prices 2 days forward (to the right side on graph)
df = df.shift(2)
print(df)

# Shift prices 1 day backward (to the left side on graph)
df = df.shift(-1)
print(df)

# Calculate previous day's price and 1-day change
df['Prev Day Price'] = df['Price'].shift(1)
df['1 day change'] = df['Price'] - df['Prev Day Price']
print(df)

# Calculate 5-day percentage return using percent change rule
df['5 day % return'] = ((df['Price'] - df['Price'].shift(5)) * 100) / df["Price"].shift(5)
print(df)

# Revert changes and keep only the 'Price' column
df = df[['Price']]
print(df)

# Change index to a date range starting from '2017-08-15' with a frequency of business days
df.index = pd.date_range(start='2017-08-15', periods=10, freq='B')
print(df.index)  # Same as above but now it has a frequency of business days

# Shift index 2 business days forward (can also use negative arguments to shift backward)
df = df.tshift(2) # tshift is used for shifting indexes
print(df)
