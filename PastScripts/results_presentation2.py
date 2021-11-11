import matplotlib.pyplot as plt
import pandas as pd

# create panda
df = pd.DataFrame({
    'Interval': ['100m', '200m', '300m', '400m', '500m'],
    'v1_time': [32, 62, 106, 143, 174],
    'v2_time': [31, 66, 112, 140, 231],
    'v3_time': [26, 58, 140, 378, 425],
})

m = df.Interval
y1 = df.v1_time
y2 = df.v2_time
y3 = df.v3_time


# Configure plot background
plt.rcParams['figure.dpi'] = 150
plt.style.use('dark_background')

# create plot

fig = plt.figure()
ax = plt.axes()
ax.plot(m, y1, linewidth=1, label='v1 Time', color='red')
ax.plot(m, y2, linewidth=1, label='v2 Time', color='blue')
ax.plot(m, y3, linewidth=1, label='v2 Time', color='green')
# Graph Presentation
ax.xaxis.grid(color='white', linestyle='dashed', which='both', alpha=0.5)
ax.yaxis.grid(color='white', linestyle='solid', which='both', alpha=0.1)
ax.set_title('Fizzbuzz to a Billion', loc='center', fontsize=16, color='Blue')
ax.set_ylabel('Time in Seconds', fontsize=12, color='Blue')
ax.set_xlabel('Number of loops', fontsize=12, color='Blue')
ax.legend(loc='lower right')
ax.fill_between(y2)


# Display Gragph
plt.show()

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
