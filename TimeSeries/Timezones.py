import pandas as pd

# Read CSV file into DataFrame
df = pd.read_csv("Excels\\msft.csv", header=1, index_col='Date Time', parse_dates=True)
print(df)

# Print index to show it's naive
print(df.index)  # this is naive

# Convert index to timezone aware datetime (US/Eastern)
df = df.tz_localize(tz="US/Eastern") # use localize to convert from naive to aware datetime
print(df.index)

# Convert timezone from US/Eastern to Europe/Berlin
df = df.tz_convert(tz="Europe/Berlin")
print(df)

# Convert timezone from Europe/Berlin to Asia/Calcutta
df = df.tz_convert(tz="Asia/Calcutta")
print(df)

# Convert index timezone from Asia/Calcutta to Africa/Cairo
df.index = df.index.tz_convert(tz="Africa/Cairo")
print(df)

# Create a datetime range with naive datetime
rng = pd.date_range(start="1/1/2017", periods=10, freq='H') # defualt is naive

# Create a datetime range with timezone aware datetime (Europe/London)
rng2 = pd.date_range(start="1/1/2017", periods=10, freq='H', tz='Europe/London')

# Create a Series with datetime index
rng3 = pd.date_range(start='2017-08-22 09:00:00', periods=10, freq="30min")
s = pd.Series(range(10), index=rng3)
print(s)

# Localize the Series to Europe/Berlin timezone
b = s.tz_localize(tz='Europe/Berlin')
print(b)

# Convert Series timezone from Europe/Berlin to Africa/Cairo
egy = b.tz_convert(tz='Africa/Cairo')
print(egy)

# Add the two timezone aware Series together
print(b + egy)
