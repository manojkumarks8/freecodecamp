import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the dataset

df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

# Create first line of best fit using all data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series(range(1880, 2051))
sea_levels_predicted = intercept + slope * years_extended
plt.plot(years_extended, sea_levels_predicted, color='red', label='Best Fit Line (All Data)')

# Create second line of best fit using data from 2000 onwards
df_2000 = df[df['Year'] >= 2000]
slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
sea_levels_predicted_2000 = intercept_2000 + slope_2000 * years_extended
plt.plot(years_extended, sea_levels_predicted_2000, color='green', label='Best Fit Line (2000 Onwards)')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save the plot as an image file
plt.savefig('sea_level_plot.png')

# Display the plot
plt.show()
