import matplotlib.pyplot as plt
import numpy as np

# Blood sugar data for one group
blood_sugar = np.array([113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129])

# Create a histogram with specified bins and styling options
plt.hist(blood_sugar, bins=[80, 100, 125, blood_sugar.max()], rwidth=0.95, color='green', edgecolor="black")
plt.show()

# Blood sugar data for two groups (Men and Women)
blood_sugar_man = np.array([113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129])
blood_sugar_woman = np.array([67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100])

# Create a grouped histogram with specified bins, styling options, and labels
plt.xlabel("Sugar Range")
plt.ylabel("Total no of patients")
plt.title("Blood Sugar analysis")
plt.hist([blood_sugar_man, blood_sugar_woman], bins=[80, 100, 125, 150], rwidth=0.95, color=["blue", "pink"],
         label=['Men', 'Women'], edgecolor="black")
# Use orientation="horizontal" to make the histogram horizontal
plt.legend()
plt.show()
