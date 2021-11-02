import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

print(plt.style.available)

# Build the DataFrame
df = pd.DataFrame({'Date': ["103121 17:30", " 103121 18:30", " 103121 19:00", "103121 19:15", " 103121 19:30",
                            "103121 20:00", "103121 20:30", "103121 21:00"],
                   'Kids': [0, 100, 210, 300, 400, 450, 500, 526]})
df['Date'] = pd.to_datetime(df['Date'])

# Configure plot background
plt.rcParams['figure.dpi'] = 150
plt.style.use('dark_background')

# create plot
fig = plt.figure()
ax = plt.axes()

# Here is a slope line
x = (df.Date[0], df.Date[7])
y = (df.Kids[0], df.Kids[7])

# Graph Presentation
ax.xaxis.grid(color='white', linestyle='dashed', which='both', alpha=0.5)
ax.yaxis.grid(color='white', linestyle='solid', which='both', alpha=0.1)
ax.set_title('Halloween Trick or Treaters over Time\n', loc='center', fontsize=16, color='orange')
ax.set_ylabel('Number of Trick of Treaters', fontsize=12, color='orange')
ax.set_xlabel('Halloween Evening', fontsize=12, color='orange')
#handels = ['slope', 'Realtime']
#labels = ['slope', 'Realtime']
#ax.legend(handels, labels, loc='lower right')
myFmt = DateFormatter("%H:%M")
ax.xaxis.set_major_formatter(myFmt)

# Run and display graph
ax.plot(x, y, linestyle='--', label='slope', color='green')
ax.plot(df.Date, df.Kids, linewidth=3, label='Realtime', color='red')
plt.show()
