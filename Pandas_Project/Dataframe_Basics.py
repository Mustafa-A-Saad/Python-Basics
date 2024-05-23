# Dataframe = represent data with row and columns ( tabular or Excel spreadsheets )
import pandas as pd

# Read data from a CSV file into a DataFrame
df = pd.read_csv("Excels\\weather.csv")  # You can import an excel file
print(df)

# Alternatively, create a DataFrame manually from a dictionary and print it
weather_data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', '1/5/2017', '1/6/2017'],
    'temp': [32, 35, 28, 24, 32, 31],
    'windspeed': [6, 7, 2, 7, 4, 2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}
df = pd.DataFrame(weather_data)  # Convert dictionary to DataFrame
print(df)

# df = pd.read_excel('',"Sheet1") for .xlsx files
# you can create dataframes from tuples or dict or (lists AND dict )


# Print the shape of the DataFrame (number of rows and columns)
print(df.shape)
rows, column = df.shape  # Assign the number of rows and columns to variables
print(rows), print(column)

# Print the first 3 rows of the DataFrame # starting from top
print(df.head(3))

# Print the last row of the DataFrame # starting from bottom
print(df.tail(1))

# Print rows from index 2 to 4
print(df[2:5])

# Print the column names of the DataFrame
print(df.columns)

# Print the 'day' column
print(df.day)

# Print the 'event' column
print(df['event'])

# Check the type of the 'event' column
print(type(df.event))

# Print selected columns ('event', 'day', 'temp')
print(df[['event', 'day', 'temp']]) # don't forget to add extra []

# Print the maximum temperature
print(df['temp'].max())

# Print the mean temperature
print(df['temp'].mean())

# Print the standard deviation of temperature
print(df['temp'].std())

# Print descriptive statistics of the DataFrame
print(df.describe())

# Print rows where temperature is greater than or equal to 32
print(df[df.temp >= 32])

# Print the row where temperature is maximum
print(df[df.temp == df['temp'].max()])

# Print the day when the temperature is maximum
print(df['day'][df.temp == df['temp'].max()])

# Print the day and temperature when temperature is maximum
print(df[['day', 'temp']][df.temp == df.temp.max()])

# Set the index of the DataFrame to 'day'
print(df.index)  # Print the default index
df.set_index('day', inplace=True)  # Set 'day' as index
print(df)  # Print DataFrame with 'day' as index
print(df.loc[['1/3/2017']])  # Access row by index label

# Reset the index of the DataFrame
df.reset_index(inplace=True)  # Reset index to default
print(df)

# Set the index of the DataFrame to 'event'
df.set_index('event', inplace=True)  # Set 'event' as index
print(df.loc['Snow']) # Access rows with 'event' as index # if 2 index have same name it prints both # .loc is for index
