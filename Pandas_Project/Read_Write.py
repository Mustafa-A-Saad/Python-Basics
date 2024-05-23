import pandas as pd

# Reading and Some functions for .csv
df = pd.read_csv("Excels\\stocks.csv")
# df = pd.read_csv("stocks.csv", nrows=3)  # reads first 3 rows excluding headers
# df = pd.read_csv('stocks.csv', skiprows=1) # skips first line ( for ex if u have extra row )
# df = pd.read_csv('stocks.csv', header=1) # starts at header 1 ( same as above )
# df = pd.read_csv('stocks.csv', header=None,names=["ticker","eps","revenue","price","people"]) # if there is no headers you can name headers
print(df)

# Data Munging = Data Cleaning
# df = pd.read_csv("stocks.csv",
#                na_values=["not available", "n.a."])  # Fills whatever keyword passed in na_values [] to NaN
df = pd.read_csv("Excels\\stocks.csv", na_values={  # Read the CSV file, replacing specified values with NaN (Not a Number)
    'eps': ["not available", 'n.a.'],
    'reveune': ['not available', "n.a.", -1],
    'people': ["not available", 'n.a.']
})
print(df)

# Writing inside a file
df.to_csv("Excels\\new.csv",
          index=False)  # creates new file and duplicates the df. to it ( index = false ) to remove the index 0,1,2,3
print(df.columns)
df.to_csv("Excels\\new.csv", columns=['tickers', 'eps'])  # i can duplicate only 2 columns


# df.to_csv("new.csv",header=False) # you can import without headers


# -------------------Reading and Writing to Excel----------------#

# Define a function to convert the 'people' column
def convert_people(cell):
    # If the cell value is "n.a.", replace it with 'sam walton'
    if cell == "n.a.":
        return 'sam walton'
    # Otherwise, return the cell value unchanged
    return cell


# Define a function to convert the 'eps' column
def convert_eps(cell):
    # If the cell value is "not available", replace it with None
    if cell == "not available":
        return None
    # Otherwise, return the cell value unchanged
    return cell


# Use converters to apply conversion functions to specific columns
# df = pd.read_excel("stocks.xlsx", "stocks", converters={
#    'people': convert_people,  # Apply the convert_people function to the 'people' column
#    'eps': convert_eps         # Apply the convert_eps function to the 'eps' column
# })

df = pd.read_excel("Excels\\stocks.xlsx", "stocks", converters={  # same as above but without functions ( lambda functions )
    'people': lambda x: "sam walton" if x == "n.a." else x,
    'eps': lambda x: None if x == "not available" else x
})
print(df)

# Writing to a new Excel

df.to_excel("Excels\\news.xlsx", "stocks", index=False)

# How to combine 2 excels to 1 Excel
df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather = pd.DataFrame({
    'day': ['1/1/2017', "1/2/2017", '1/3/2017'],
    'temp': [32, 35, 28],
    'event': ["Rain", 'Sunny', "Snow"]
})

with pd.ExcelWriter('Excels\\stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")
