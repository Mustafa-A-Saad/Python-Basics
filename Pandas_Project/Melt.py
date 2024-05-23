import pandas as pd


df = pd.read_csv("Excels\\us_temp.csv")

# Melting the DataFrame to convert it from wide( Y Axis ) to long ( X Axis ) format
# 'day' column will be kept as an identifier variable (id_vars)
# 'city' column headers will be melted into a single column (var_name)
# Corresponding temperature values will be melted into another column (value_name)
df1 = pd.melt(df, id_vars=["day"], var_name="city", value_name="temp")
print(df1)

# Printing only the rows where the city is "chicago"
print(df1[df1["city"] == "chicago"])
