import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6, 7]
y = [50, 51, 52, 48, 47, 49, 46]

# Basic Line Plot
plt.plot(x, y, color="green", linewidth=5, linestyle='dashed')
plt.xlabel("Day")
plt.ylabel("Temp")
plt.title("Weather")
plt.show()

# ---------Formatting-----#

# Line plot with different formatting options
plt.plot(x, y, color="red", marker="D", linestyle="dashed")
plt.show()

# Shortened version using shorthand notation
plt.plot(x, y, 'rD--')
plt.show()

# Using alpha to control transparency
plt.plot(x, y, color='green', alpha=0.7)
plt.show()
