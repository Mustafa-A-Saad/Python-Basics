import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips_data = pd.read_csv('Excels\\tips.csv')

# Duplicates and NA values
print(tips_data.isnull().sum())
tips_data.drop_duplicates(inplace=True)
print(tips_data.describe())

# Line Plot for tips
tips_data.tip.plot()
plt.show()

# Histogram Plot for total bill
plt.hist(tips_data['total_bill'], bins=15, color='green', edgecolor='black')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.title("Histogram for Total_bill")
plt.show()

# Pairplot EDA
sns.pairplot(tips_data, hue='sex')
plt.show()

# Heatmap
numeric_cols = tips_data.select_dtypes(include='number').columns # Includes only numerical columns
plt.figure(figsize=(12, 8))
sns.heatmap(tips_data[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
