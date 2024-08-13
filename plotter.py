import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('jump.xlsx')
x_values = np.arange(1, len(df) + 1) * 25/1000
# Assume the data has columns 'Date', 'Value1', 'Value2', 'Value3'
plt.plot(x_values, df['X:'], label='X')
plt.plot(x_values, df['Y:'], label='Y')
plt.plot(x_values, df['Z:'], label='Z')

# Add title, labels, and legend
plt.title('Jump Data', fontsize=15)
plt.xlabel('Time', fontsize=15)
plt.ylabel('Acceleration', fontsize=15)
plt.legend()

# Show the plot
plt.show()