import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn has built-in datasets. Uncomment the line below to see available datasets.
# print(sns.get_dataset_names())

# Load 'car_crashes' dataset from Seaborn
crash_df = sns.load_dataset('car_crashes')

# -------Distribution Plot-----#

# Create a distribution plot for the 'not_distracted' column
sns.distplot(crash_df['not_distracted'], kde=False, bins=25)
# KDE = Kernel Density Estimation
plt.show()

# -----Joint Plot (Scatter Plot)-----#

# Create a joint plot (scatter plot) for 'speeding' and 'alcohol' columns with kernel density estimation
sns.jointplot(x='speeding', y='alcohol', data=crash_df, kind='kde')
# 'kind' parameter can be 'kde', 'reg' (regression), 'hex' (hexbin plot)
plt.show()

# -------KDE Plot-----#

# Create a KDE plot for the 'alcohol' column
sns.kdeplot(crash_df['alcohol'])
plt.show()

# ----Pair Plot----#

# Load 'tips' dataset from Seaborn
tips_df = sns.load_dataset("tips")
# Create a pair plot for numerical columns in 'tips_df', with hue as 'sex' and color palette for hue categories
sns.pairplot(tips_df, hue='sex', palette=['blue', 'pink'])
plt.show()

# ----Rug Plot----#

# Create a rug plot for the 'tip' column in 'tips_df'
sns.rugplot(tips_df['tip'])
plt.show()
