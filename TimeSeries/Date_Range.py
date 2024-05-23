import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV doesn't have dates
# Reading CSV file into a DataFrame
df = pd.read_csv("Excels\\aapl2.csv")
print(df.head())  # Printing first few rows of DataFrame

# Generating a date range for June 2017 with business days frequency
rng = pd.date_range(start="2017-06-01", end="2017-06-30", freq="B")  # B = business Days
# OR
# rng = pd.date_range(start="2017-06-1", periods=72, freq="H") from start to peroid which is 72 (freq)

# Setting the index of the DataFrame to the generated date range
df.set_index(rng, inplace=True)
print(df)  # Printing DataFrame with updated index

# Slicing the DataFrame for the date range from June 1, 2017 to June 10, 2017
print(df["2017-06-01":"2017-06-10"])

# Calculating the mean of the 'Close' column for the sliced date range
print(df["2017-06-01":"2017-06-10"].Close.mean())

# Resampling the DataFrame to daily frequency and forward-filling missing values
print(df.asfreq('D', method='ffill'))  # includes the weekends
# Resampling the DataFrame to weekly frequency and forward-filling missing values
print(df.asfreq('W', method='ffill'))  # includes the Weekly
# Resampling the DataFrame to hourly frequency and forward-filling missing values
print(df.asfreq('H', method='ffill'))  # includes the Hourly

# Generating a time series with random integer values and the defined date range
ts = pd.Series(np.random.randint(1, 10, len(rng)), index=rng)

# Plotting the 'Close' column of the DataFrame
df.Close.plot()
plt.show()
