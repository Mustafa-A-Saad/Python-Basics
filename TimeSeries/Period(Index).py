import pandas as pd

# Creating Period objects

# Yearly period, default frequency is 'A-DEC' (Annual, ending in December)
y = pd.Period('2016')
print(y)
print(dir(y))  # Listing attributes and methods of the Period object

# Start and end times of the year period
print(y.start_time)  # 1st January of the year
print(y.end_time)  # 31st December of the year

# Monthly period, frequency set to 'M' (Month)
m = pd.Period('2011-1', freq='M')
print(m)
print(m.start_time)  # 1st January of the month
print(m.end_time)  # 31st January of the month

# Performing operations on periods
print(m + 1)  # Adding one month to the period ('2011-02')

# Period objects handle leap years
d = pd.Period('2016-02-28',freq="D")  # default frequency is 'D' (Day)
print(d + 1)  # Output is '2016-02-29' because 2016 was a leap year

# Hourly period, frequency set to 'H' (Hour)
h = pd.Period('2016-02-28 23:00:00', freq='H')
print(h.start_time)  # Start of the hour
print(h.end_time)  # End of the hour

# Quarterly periods
q = pd.Period('2017Q1')  # Calendar year ends in December by default
print(q.start_time)
print(q.end_time)

# Fiscal year ending in January
q2 = pd.Period('2017Q1', freq='Q-JAN')
print(q2.start_time)  # Fiscal year starts from February
print(q2.end_time)  # Fiscal year ends on April 30th

# Creating Period Index

print()

import numpy as np

# Generating a period index for quarters
idx = pd.period_range('2011', '2017', freq='Q')
print(idx)

# Creating a Series with random values and Period Index
idx2 = pd.period_range('2011', periods=10, freq='Q-JAN')
ps = pd.Series(np.random.randn(len(idx2)), idx2)
print(ps)
print(ps.index)

# Slicing based on period index
print(ps['2011':'2013'])

# Converting Period Index to TimeIndex and back
pst = ps.to_timestamp()  # Converting PeriodIndex to TimeIndex
print(pst)
print(pst.index)

# Converting TimeIndex back to Period Index
pst = pst.to_period()
print(pst.index)


#--------Period Index---------#

import numpy as np

idx = pd.period_range('2011','2017',freq='Q')
print(idx)

idx2 = pd.period_range('2011',periods=10,freq='Q-JAN')

ps = pd.Series(np.random.randn(len(idx2)), idx2)
print(ps)
print(ps.index)


print(ps['2011':'2013'])

pst = ps.to_timestamp() # converts from peroid index to TimeIndex
print(pst)
print(pst.index)

pst = pst.to_period()
print(pst.index) # from TimeIndex to Peroid

#---Small lil project---#

import pandas as pd


df = pd.read_csv("Excels\\wmt.csv")
print(df)

# Set "Line Item" as the index
df.set_index("Line Item", inplace=True)

# Transpose the DataFrame (switch rows and columns)
df = df.T
print(df)

# Print the index of the transposed DataFrame
print(df.index)

# Convert index to PeriodIndex with frequency 'Q-JAN' (Quarterly, starting in January)
df.index = pd.PeriodIndex(df.index, freq='Q-JAN')
print(df.index)

# Extract the start date from the PeriodIndex
df['start date'] = df.index.map(lambda x: x.start_time)  # Get the start time of the period
print(df)

# Extract the end date from the PeriodIndex and normalize to remove the hour stamp
df['end date'] = df.index.map(lambda x: x.end_time.normalize())
print(df)





