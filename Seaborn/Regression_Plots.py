import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets from Seaborn
crash_df = sns.load_dataset('car_crashes')
tips_df = sns.load_dataset('tips')
flights_df = sns.load_dataset('flights')
iris = sns.load_dataset('iris')
att_df = sns.load_dataset('attention')

# Set the figure size and context for the plots
plt.figure(figsize=(8, 6))
sns.set_context('paper', font_scale=1.3)

# Create a scatter plot with a regression line using lmplot for 'total_bill' and 'tip' in 'tips_df'
# Color points based on 'sex', use custom markers and adjust scatter plot aesthetics
sns.lmplot(x='total_bill', y='tip', hue='sex', data=tips_df, markers=['o', '^'],
           scatter_kws={'s': 100, 'linewidths': 0.5, 'edgecolor': "black"})
plt.show()

# ---Another---#

# Create multiple scatter plots with regression lines for 'total_bill' and 'tip' in 'tips_df'
# Separate plots for different combinations of 'sex' and 'time'
sns.lmplot(x='total_bill', y='tip', col='sex', row='time', data=tips_df)
plt.show()
