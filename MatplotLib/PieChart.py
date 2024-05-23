import matplotlib.pyplot as plt

# Expense values and labels
exp_vals = [1600, 600, 300, 410, 250]
exp_labels = ["Home Rent", 'Food', 'Phone/Internet Bill', 'Car', 'Others']

# Create a pie chart with specified parameters
plt.pie(exp_vals, labels=exp_labels, radius=1.3, autopct="%0.2f%%", explode=[0.1, 0.1, 0.1, 0.1, 0.1], startangle=45)
# radius to make the circle bigger
# autopct to show percentage with 2 decimal places
# explode to emphasize certain slices by pulling them out
# startangle rotates the center angle around which rotates the circle to the specific (45) degree

plt.axis("equal")  # to make the pie chart look like an equal circle

# Save the pie chart as a PNG file with specified parameters
plt.savefig("PieChart.png", bbox_inches='tight', pad_inches=2, transparent=True)
# bbox to make it fit tightly to the png
# pad to add padding around it
# Transparent to make the background transparent (good for websites and etc.)

plt.show()
