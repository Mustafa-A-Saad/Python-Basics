import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load 'car_crashes' and 'tips' datasets from Seaborn
crash_df = sns.load_dataset('car_crashes')
tips_df = sns.load_dataset('tips')

# ----Bar Plot---- #

# Create a bar plot for the median 'total_bill' by 'sex' in 'tips_df'
sns.barplot(x='sex', y='total_bill', data=tips_df, palette=['blue', 'pink'], estimator=np.median)
plt.show()

# ---Count Plot--- #

# Create a count plot for the frequency of each category in 'sex' column in 'tips_df'
sns.countplot(x='sex', data=tips_df, palette=['blue', 'pink'])
plt.show()

# ---Box Plot--- #

# Create a box plot for 'total_bill' grouped by 'day' and separated by 'sex' in 'tips_df'
sns.boxplot(x="day", y="total_bill", data=tips_df, hue='sex', palette=['blue', 'pink'])
plt.show()

# ----Violin Plot---- #

# Create a violin plot for 'total_bill' grouped by 'day' and separated by 'sex' in 'tips_df'
# Violin plot uses KDE estimation to show the distribution
sns.violinplot(x='day', y='total_bill', data=tips_df, hue='sex', split=True)
# 'split' is used to compare between categories in one spot (remove it to see the difference)
plt.show()

# ----Strip Plot---- #

# Create a strip plot for 'total_bill' grouped by 'day' and separated by 'sex' in 'tips_df'
plt.figure(figsize=(8, 5))
sns.stripplot(x='day', y='total_bill', data=tips_df, hue='sex', jitter=True, dodge=True)
# Jitter is used to make the dots a little further out, and dodge separates data of males and females
plt.show()

# ----Swarm Plot---- #

# Create a swarm plot for 'total_bill' grouped by 'day' in 'tips_df'
sns.swarmplot(x='day', y='total_bill', data=tips_df, color='white')
plt.show()
