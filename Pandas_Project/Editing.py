import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv('Excels\\weather3.csv')
print(df)

# Replace specific values in DataFrame with NaN
new_df = df.replace([-999999, -888888], np.NaN)
print(new_df)

# Replace specific values for different columns with NaN
new_df = df.replace({
    'temp': [-999999, -888888],  # Replace in 'temp' column
    'windspeed': -999999,         # Replace in 'windspeed' column
    'event': "0"                  # Replace in 'event' column
}, np.NaN)
print(new_df)

# Replace specific values with NaN or another value
new_df = df.replace({
    -999999: np.NaN,       # Replace -999999 with NaN
    'No Event': 'Sunny'   # Replace 'No Event' with 'Sunny'
})
print(new_df)

# Replace alphabetic characters in 'temp' and 'windspeed' columns with a space
new_df = df.replace({
    'temp': "[A-Za-z]",       # Replace alphabetic characters in 'temp' column
    'windspeed': "[A-Za-z]"   # Replace alphabetic characters in 'windspeed' column
}, " ", regex=True)
print(new_df)

# Create a DataFrame
df = pd.DataFrame({
    'score': ['exceptional', 'average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
print(df)

# Replace categorical values with numerical values
new_df = df.replace(['poor', 'average', 'good', 'exceptional'], [1, 2, 3, 4])
print(new_df)
