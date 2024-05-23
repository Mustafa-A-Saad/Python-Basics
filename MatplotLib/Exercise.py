import matplotlib.pyplot as plt

# Company and Revenue data
company = ['GOOGL', 'AMZN', 'MSFT', 'FB']
revenue = [90, 136, 89, 27]

# Create a bar chart
plt.bar(company, revenue, edgecolor="black", color="g")

# Save the plot as a PNG file with specified parameters
plt.savefig("exc.png", bbox_inches="tight", pad_inches=2, transparent=True)

# Save the plot as a PDF file
plt.savefig("exc.pdf")

# Display the plot
plt.show()
