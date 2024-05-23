import pandas as pd

# First example: Merging two DataFrames based on the 'city' column
usa_df1 = pd.DataFrame({
    "city": ["new york", "chicago", "orlando"],
    "temp": [21, 14, 35]
})

usa_df2 = pd.DataFrame({
    "city": ["chicago", "orlando", "new york"],
    "humidity": [65, 68, 75]
})

# Merging usa_df1 and usa_df2 on the 'city' column
merged_df = pd.merge(usa_df1, usa_df2, on="city")
print(merged_df)

# Second example: Merging with outer join and indicator
usa_df1 = pd.DataFrame({
    "city": ["new york", "chicago", "orlando", "baltimore"],
    "temp": [21, 14, 35, 32]
})

usa_df2 = pd.DataFrame({
    "city": ["chicago", "san francisco", "new york"],
    "humidity": [65, 68, 75]
})

# Merging usa_df1 and usa_df2 on the 'city' column with outer join and indicator set to True
merged_df = pd.merge(usa_df1, usa_df2, on="city", how="outer", indicator=True)
print(merged_df)

# Third example: Merging when columns have the same name in both DataFrames
usa_df1 = pd.DataFrame({
    "city": ["new york", "chicago", "orlando", "baltimore"],
    "temp": [21, 14, 35, 32],
    "humidity": [65, 68, 71, 75]
})

usa_df2 = pd.DataFrame({
    "city": ["chicago", "new york", "san diego"],
    "temp": [21, 14, 35],
    "humidity": [65, 68, 71]
})

# Merging usa_df1 and usa_df2 on the 'city' column
merged_df = pd.merge(usa_df1, usa_df2, on="city")
print(merged_df)
