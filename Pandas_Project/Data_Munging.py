import pandas as pd

# Read the CSV file "weather2.csv" and parse the dates in the "day" column to timestamps
df = pd.read_csv("Excels\\weather2.csv", parse_dates=["day"])
print(type(df.day[0]))  # Print the type of the first element in the "day" column
df.set_index("day", inplace=True)  # Set the "day" column as the index of the DataFrame
print(df)

# Fill missing values in the DataFrame with specific values
new_df = df.fillna({
    "temp": 0,  # Fill missing values in the "temp" column with 0
    'windspeed': 0,  # Fill missing values in the "windspeed" column with 0
    'event': 'No Event'  # Fill missing values in the "event" column with 'No Event'
})
print(new_df)

# Fill missing values using forward fill method
new_df = df.fillna(method="ffill")  # Takes the value above it for itself vertically
print(new_df)

# Fill missing values using backward fill method along columns
new_df = df.fillna(method="bfill", axis="columns")  # bfill = takes value below it , but here horizontally because axis
print(new_df)

# Fill missing values using forward fill method with a limit of 1 consecutive NaN value
new_df = df.fillna(method="ffill", limit=1)  # limit here means can ffill only once to a NaN value
print(new_df)

# Interpolate missing values using linear interpolation
new_df = df.interpolate()  # completes the NaN values between by taking mean of after and before
print(new_df)

# Interpolate missing values based on time
new_df = df.interpolate(method="time")  # completes NaN values but according to time
print(new_df)

# Drop rows with at least one NaN value
new_df = df.dropna()  #
print(new_df)

# Drop rows where all columns are NaN
new_df = df.dropna(how="all")
print(new_df)

# Drop rows that have at least 2 non-NaN values
new_df = df.dropna(thresh=2)
print(new_df)

# Reindex the DataFrame with a new DatetimeIndex
dt = pd.date_range("01-01-2017", "01-11-2017")
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)  # Adding the missing dates
print(df)
