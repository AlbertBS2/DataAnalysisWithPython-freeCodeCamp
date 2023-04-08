import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    x = df['Year'].to_numpy()
    y = df['CSIRO Adjusted Sea Level'].to_numpy()

    # Create scatter plot
    plt.scatter(x, y)

    # Create first line of best fit
    years_extended = np.arange(1880, 2051)

    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    line = [slope * xi + intercept for xi in years_extended]

    plt.plot(years_extended, line, label='Fitting Line', c='k')
    plt.scatter(x, y)

    # Create second line of best fit
    years_extended_2 = np.arange(2000, 2051)

    slope, intercept, r_value, p_value, std_err = linregress(x[120:], y[120:])

    line = [slope * xi + intercept for xi in years_extended_2]

    plt.plot(years_extended_2, line, label='Fitting Line', c='k')
    plt.scatter(x, y)

    # Add labels and title
    plt.title('Rise in Sea Level')

    plt.xlabel('Year')

    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()