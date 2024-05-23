import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load various datasets from Seaborn
crash_df = sns.load_dataset('car_crashes')
tips_df = sns.load_dataset('tips')
flights_df = sns.load_dataset('flights')
att_df = sns.load_dataset('attention')
iris = sns.load_dataset('iris')

print(flights_df.head())

# ---HeatMaps--#

# Create a heatmap for the correlation matrix of numerical columns in 'crash_df'
plt.figure(figsize=(8, 6))
sns.set_context('paper', font_scale=1.4)
numeric_columns = crash_df.select_dtypes(include=[np.number]).columns
crash_df_numeric = crash_df[numeric_columns]
crash_mx = crash_df_numeric.corr()
sns.heatmap(crash_df_numeric.corr(), annot=True, cmap='Blues')
plt.show()

# ----Another Heatmap Explanation----#

# Pivot the 'flights_df' to create a heatmap of passengers by month and year
flights_df = flights_df.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(flights_df, cmap='Blues', linecolor='white', linewidth=1)
plt.show()

# ----Cluster Maps----#

# Create a cluster map for the 'iris' dataset
species = iris.pop('species')
sns.clustermap(iris)
plt.show()

# --Another Explanation--#

# Pivot the 'flights_df' and create a cluster map with standard scaling
flights_df = flights_df.pivot_table(index='month', columns='year', values='passengers')
sns.clustermap(flights_df, cmap='Blues', standard_scale=1)
plt.show()

# ---PairGrid---#

# Create a PairGrid for the 'iris' dataset with scatter plots, histograms, and KDEs
iris_g = sns.PairGrid(iris, hue='species')
iris_g.map_diag(plt.hist)
iris_g.map_upper(plt.scatter)
iris_g.map_lower(sns.kdeplot)
plt.show()

# With defining x and y Axis
iris_g = sns.PairGrid(iris, hue='species', x_vars=['sepal_length', 'sepal_width'],
                      y_vars=['petal_length', 'petal_width'])
iris_g.map(plt.scatter)
iris_g.add_legend()
plt.show()

# ---Facet Grid---#

# Create a FacetGrid for the 'tips_df' dataset with histograms based on time and smoker status
tips_fg = sns.FacetGrid(tips_df, col='time', row='smoker')
tips_fg.map(plt.hist, 'total_bill', bins=8)
plt.show()

# ---Another----#

# Create a FacetGrid for 'tips_df' with scatter plots based on time, smoker status, and palette
tips_fg = sns.FacetGrid(tips_df, col='time', hue='smoker', height=4, aspect=1.2, palette='Set1')
tips_fg.map(plt.scatter, 'total_bill', 'tip', edgecolor="white")
plt.show()

#---Another---#

# Create a FacetGrid for 'tips_df' with scatter plots based on sex, smoker status, and custom markers
kws = dict(s=50, linewidth=0.5, edgecolor='white')
tips_fg = sns.FacetGrid(tips_df, col='sex', hue='smoker', height=4, aspect=1.2, hue_order=['Yes', 'No'],
                        hue_kws=dict(marker=["^", 'v']))
tips_fg.map(plt.scatter, 'total_bill', 'tip', **kws)
plt.show()

#----Another---#

# Create a FacetGrid for 'att_df' with line plots based on subject and solutions
att_fg = sns.FacetGrid(att_df, col='subject', col_wrap=5, height=1.5)
att_fg.map(plt.plot, 'solutions', 'score', marker='.')
plt.show()
