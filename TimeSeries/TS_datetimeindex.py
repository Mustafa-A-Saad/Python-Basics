import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and parse dates
df = pd.read_csv("Excels\\aapl.csv", parse_dates=["Date"], index_col="Date")

# Print the first 5 rows of the DataFrame
print(df.head(5))

# Print data for July 2017
print(df.loc['2017-07'])

# Print the Close price for January 2017
print(df.loc["2017-01"].Close)

# Calculate and print the average Close price for February 2017
print(df.loc['2017-02'].Close.mean())


# Sort the index
df.sort_index(inplace=True)
# Calling df.sort_index(inplace=True) before slicing the DataFrame ensures that the index is sorted in ascending order,
# allowing slicing operations to work correctly,
# as slicing requires the index to be sorted.

# Print data for the date range from January 1, 2017 to January 7, 2017
print(df.loc["2017-01-01":"2017-01-07"])

#-----Resampling-----#

# Plotting the closing price without resampling (plots on a daily basis)
df.Close.plot()
plt.show()

# Resample the data to get mean Close price for each month and plot
print(df.Close.resample("M").mean())  # M for month
df.Close.resample("M").mean().plot()
plt.show()

# Resample the data to get mean Close price for each week and plot
df.Close.resample("W").mean().plot()  # W for week
plt.show()

# Resample the data to get mean Open price for each quarter and plot
df.Open.resample("Q").mean().plot()  # Q for quarter
plt.show()

# Resample the data to get mean Open price for each quarter and plot as bar chart
df.Open.resample("Q").mean().plot(kind="bar")  # Q for quarter
plt.show()
