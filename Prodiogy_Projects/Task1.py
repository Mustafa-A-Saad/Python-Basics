import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


population_data = pd.DataFrame({
    "gender" : np.random.choice(['Male','Female'],size=1000),
    "age" : np.random.normal(loc=30,scale=5,size=1000).astype(int)
})


sns.pairplot(population_data,hue="gender")
plt.show()

plt.figure(figsize=(10,8))

plt.subplot(1,2,1)
sns.countplot(x='gender',data=population_data,palette=['pink', 'skyblue'])
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.show()


plt.hist(population_data['age'], bins=15, color='green', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title("Histogram for Age Distrubtion")
plt.show()

