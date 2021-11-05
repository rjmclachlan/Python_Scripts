import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

df = pd.DataFrame({
    'Interval': ['100m', '200m', '300m', '400m', '500m'],
    'v1_time': [38, 82, 114, 162, 195],
    'v2_time': [36, 74, 111, 138, 190],
})

# Configure plot background
plt.rcParams['figure.dpi'] = 150
plt.style.use('seaborn')

# create plot
fig = plt.figure()
ax = plt.axes()
ax.plot(df.Interval, df.v1_time, linewidth=1, label='v1 Time', color='red')
ax.plot(df.Interval, df.v2_time, linewidth=1, label='v2 Time', color='blue')

# Graph Presentation

ax.xaxis.grid(color='white', linestyle='dashed', which='both', alpha=0.5)
ax.yaxis.grid(color='white', linestyle='solid', which='both', alpha=0.1)
ax.set_title('Fizzbuzz to a Billion', loc='center', fontsize=16, color='Blue')
ax.set_ylabel('Time in Seconds', fontsize=12, color='Blue')
ax.set_xlabel('Number of loops', fontsize=12, color='Blue')
# myFmt = DateFormatter("%H:%M")
# ax.xaxis.set_major_formatter(myFmt)
"""
plt.xscale('log')
plt.yscale('log')

# specify x-axis labels
x_ticks = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
x_labels = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
plt.xticks(ticks=x_ticks, labels=x_labels, fontsize=8)

y_ticks = [.0005, .005, 5]
y_labels = [.0005, .005, 5]
plt.yticks(ticks=y_ticks, labels=y_labels)
"""

ax.legend(loc='lower right')
# Display graph1
plt.show()
