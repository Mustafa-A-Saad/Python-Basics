import numpy as np
import pandas as pd

# Create DataFrames for weather in India and the US
india_weather = pd.DataFrame({
    "city": ["mumbai", "delhi", "bangalore"],
    "temp": [32, 45, 30],
    "humidity": [80, 60, 78]
})

us_weather = pd.DataFrame({
    "city": ["new york", "chicago", "orlando"],
    "temp": [21, 14, 35],
    "humidity": [68, 65, 75]
})

# Concatenate the two DataFrames
combined_weather = pd.concat([india_weather, us_weather], ignore_index=True)
print(combined_weather)

# Concatenate with keys
combined_weather = pd.concat([india_weather, us_weather],
                             keys=["india", "US"])  # adds a new index on the left next to (0,1,2,...)
print(combined_weather)

# Access data for the US
print(combined_weather.loc["US"])  # because we delcared keys US as an index we can use .loc

# Create DataFrames for temperature and windspeed
temp_df = pd.DataFrame({
    "city": ["mumbai", "delhi", "bangalore"],
    "temp": [32, 45, 30],
}, index=[0, 1, 2])

windspeed_df = pd.DataFrame({
    "city": ["delhi", "mumbai", np.nan],  # Use np.nan to represent NaN values
    "windspeed": [7, 12, np.nan]  # Use np.nan to represent NaN values
}, index=[1, 0, 2])

# Concatenate the two DataFrames
df = pd.concat([temp_df, windspeed_df], axis=1)  # axis=1 to concat to the side of each other
print(df)

# Create a Series for events
s = pd.Series(["Humid", "Dry", "Rain"], name="event")  # creates a new Column
# Concatenate the temperature DataFrame and the event Series
df = pd.concat([temp_df, s], axis=1)
print(df)
