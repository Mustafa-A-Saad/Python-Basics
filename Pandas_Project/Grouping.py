import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Excels\\weather4.csv")
print(df)

# Group the DataFrame by the 'city' column
g = df.groupby("city")  # groups all duplicates names in city column together
# Print the grouped object
print(g) # returns an object which contains the new Dataframe with cities groupedby

# Iterate over each group
for city, city_df in g:
    print(f"THIS IS THE CITIES {city}")  # Print the city name
    print(city_df)  # Print the DataFrame corresponding to the current city

# Get the DataFrame for the city 'mumbai'
print(g.get_group('mumbai'))

# Find the maximum value for each city
print(g.max())

# Compute the mean for numeric columns for each city
print(g.mean(numeric_only=True))

# Generate descriptive statistics for each city group
print(g.describe())

# Plot each group separately
g.plot() # must do this to add plt.show()
plt.show()  # Display the plots
