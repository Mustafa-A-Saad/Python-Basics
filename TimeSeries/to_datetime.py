import pandas as pd

# List of date strings in various formats
dates = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2017', '2017.01.05', '2017/01/05', '20170105']

# Convert the list of date strings to Pandas DateTime objects
print(pd.to_datetime(dates))  # default format is MM/DD/YYYY

# US = mm/dd/yyyy
# Europe = dd/mm/yyyy

# Conversion with default format (US format assumed)
print(pd.to_datetime('5/1/2017'))  # default converts to USA format

# Conversion with dayfirst=True to force interpretation as European format

print(pd.to_datetime('5/1/2017', dayfirst=True))  # converts to Europe

# Conversion with a custom format specified
print(pd.to_datetime('5$1$2017', format='%d$%m$%Y'))  # cpd.ustom format

# Handling errors using errors parameter

# List of date strings including invalid and valid dates
dates = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2017', '2017.01.05', '2017/01/05', '20170105', 'abc']

# 'ignore' mode: Ignore invalid strings, leave them as they are
print(pd.to_datetime(dates, errors='ignore'))  # not practical (doesn't perform any conversion)

# 'coerce' mode: Convert invalid strings to NaT (Not a Time)
print(pd.to_datetime(dates, errors='coerce'))  # invalid strings will convert to NaT

# Conversion from epoch time to datetime
t = 1501356749  # epoch time
print(pd.to_datetime(t, unit='s'))  # default unit='ns' which is nanoseconds
dt = pd.to_datetime([t], unit='s')

# Converting from real time to epoch time
print(dt.view('int64'))  # converts from real time to epoch time
