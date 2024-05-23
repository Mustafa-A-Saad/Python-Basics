import matplotlib.pyplot as plt
import numpy as np

# ----Basics----#

# Sample weather data
days = [1, 2, 3, 4, 5, 6, 7]
max_t = [50, 51, 52, 48, 47, 49, 46]
min_t = [43, 42, 40, 44, 33, 35, 37]
avg_t = [45, 48, 48, 46, 40, 42, 21]

# Create a line plot for max, min, and avg temperatures
plt.plot(days, max_t, label='Max Temp')
plt.plot(days, min_t, label="Min Temp")
plt.plot(days, avg_t, label="Avg")
plt.legend(loc='upper right', shadow=True, fontsize="small")
plt.grid()
plt.xlabel("Days")
plt.ylabel('Temperature')
plt.title("Weather")
plt.show()

# ------Bar Chart------#

# Sample company revenue and profit data
company = ['GOOGL', 'AMZN', 'MSFT', 'FB']
revenue = [90, 136, 89, 27]
profit = [40, 2, 34, 12]

xpos = np.arange(len(company))  # you must do this before doing a bar because bar can't take Strings
plt.xticks(xpos, company)  # replace the array [0,1,2,3,4] with corresponding element in company
plt.bar(xpos - 0.2, revenue, width=0.4, label='Revenue')
plt.bar(xpos + 0.2, profit, width=0.4, label='Profit')
plt.legend()
plt.show()

# ---Horziontal Bar Chart-----#

plt.yticks(xpos, company)  # replace the array [0,1,2,3,4] with corresponding element in company
plt.barh(xpos - 0.2, revenue, height=0.4, label='Revenue')
plt.barh(xpos + 0.2, profit, height=0.4, label='Profit')
plt.legend()
plt.show()
