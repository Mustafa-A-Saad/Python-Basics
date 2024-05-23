import pandas as pd

# Read CSV file into DataFrame
df = pd.read_csv("Excels\\aapl_no_dates.csv")
print(df.head())

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

# Define CustomBusinessDay based on US Federal holidays
usb = CustomBusinessDay(calendar=USFederalHolidayCalendar())

# Generate date range using CustomBusinessDay
rng = pd.date_range(start="2017-07-01", end="2017-07-21", freq=usb)

# Set index of DataFrame using the generated date range
df.set_index(rng, inplace=True)
print(df)

# Define custom holiday calendar for Tefa's Birthday

from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday

class MyBirthdayCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday("Tefa's Birth Day", month=2, day=7)
    ]

# Create CustomBusinessDay for custom holidays
myC = CustomBusinessDay(calendar=MyBirthdayCalendar())

# Generate date range for custom holidays
rng2 = pd.date_range(start="2017-02-01", end="2017-02-21", freq=myC)

# Set index of DataFrame using the generated date range for custom holidays
df.set_index(rng2, inplace=True)
print(df)

# Define CustomBusinessDay for Egypt with Sundays and Mondays as business days and a specific holiday
egypt = CustomBusinessDay(weekmask="Sun Mon Tue Wed Thu", holidays=["2017-07-13"])

# Generate date range for Egypt using the defined CustomBusinessDay
rng3 = pd.date_range(start="2017-07-01", periods=14, freq=egypt)

# Set index of DataFrame using the generated date range for Egypt
df.set_index(rng3, inplace=True)
print(df)
