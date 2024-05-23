import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets from Seaborn
crash_df = sns.load_dataset('car_crashes')
tips_df = sns.load_dataset('tips')

# Set Seaborn style and context
sns.set_style('darkgrid')  # Set the overall style for the plots
sns.set_context('paper', font_scale=1.4)  # Set the context for the plots, adjusting the font scale
plt.figure(figsize=(8, 4))  # Set the size of the figure

# Create a joint plot for 'speeding' and 'alcohol' columns in 'crash_df' with a regression line
sns.jointplot(x='speeding', y='alcohol', data=crash_df, kind='reg')
# Uncomment the line below to remove the lines around the plot
# sns.despine(left=True, bottom=True)
plt.show()

# ---Palettes---#

plt.figure(figsize=(8, 5))  # Set the size of the figure
sns.set_style('darkgrid')  # Set the overall style for the plots
sns.set_context('talk')  # Set the context for the plots, adjusting the font scale

# Create a strip plot for 'total_bill' by 'day' in 'tips_df' with different colors for 'sex' using the 'magma' palette
sns.stripplot(x='day', y='total_bill', data=tips_df, hue='sex', palette='magma')
plt.show()
