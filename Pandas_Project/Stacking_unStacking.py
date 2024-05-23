import pandas as pd

#-----CSV contains 2 levels of headers--------#

# Read the Excel file with two levels of headers and set the first column as index
df = pd.read_excel("Excels\\stack_stocks.xlsx", header=[0, 1], index_col=0) # index_col=0 to remove this unnamed:0_level_0
print(df)

# Stack the DataFrame along the innermost level of the column multi-index
print(df.stack())

# Stack the DataFrame along the outermost level of the column multi-index
print(df.stack(level=0))

# Stack the DataFrame along the innermost level of the column multi-index and assign to a new DataFrame
df_stacked = df.stack()
print(df_stacked)

# Unstack the stacked DataFrame to revert the stacking
df_stacked.unstack()
print(df_stacked)

#------3 levels Headers xlsx----#

# Read the Excel file with three levels of headers and set the first column as index
df2 = pd.read_excel("Excels\\stocks_3_levels.xlsx", header=[0,1,2], index_col=0)
print(df2)

# Stack the DataFrame along the innermost level of the column multi-index
print(df2.stack()) # this is same as df.stack(level=2)

# Stack the DataFrame along the outermost level of the column multi-index
print(df2.stack(level=0))

# Stack the DataFrame along the middle level of the column multi-index
print(df2.stack(level=1))
