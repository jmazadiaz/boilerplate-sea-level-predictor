import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit

    fit1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    
    xFlin , yFlin = [np.arange(df['Year'].min(),2051,1).tolist()
                     ,(np.arange(df['Year'].min(),2051,1)*fit1.slope + fit1.intercept).tolist()]
    # Plot
    plt.plot(xFlin,yFlin)
    
    # Create second line of best fit
    
    # New DataFrame
    df_L2 = df[df['Year'] >= 2000]
    
    fit2 = linregress(df_L2['Year'],df_L2['CSIRO Adjusted Sea Level'])

    xFlin2 , yFlin2 = [np.arange(2000,2051,1).tolist()
                       , (np.arange(2000,2051,1)*fit2.slope + fit2.intercept).tolist()]
    # Plot
    plt.plot(xFlin2,yFlin2)
    
    # Add labels and title
    
    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()