import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df = df.set_index('date')

# Clean data
down = df['value'].quantile(0.025)
up = df['value'].quantile(0.975)

df.loc[df['value'] <= down, 'value'] = np.nan
df.loc[df['value'] >= up, 'value'] = np.nan

df.dropna(inplace=True)


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    df_line.index = [x[:-3] for x in df_line.index]

    fig = (df_line.plot(xlabel='Date',
                        ylabel='Page Views',
                        figsize=(20, 6.2),
                        legend=None,
                        color='red',
                        title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019'))
    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = pd.read_csv("fcc-forum-pageviews.csv")
  
    df_bar['yy-mm'] = [x[:7] for x in df_bar['date']]

    df_bar_end = df_bar.groupby(['yy-mm']).mean()
    df_bar_end['Years'] = [x[:4] for x in df_bar_end.index]
    df_bar_end['Months'] = [x[5:7] for x in df_bar_end.index]
    df_bar_end = df_bar_end.rename({'value':'Average Page Views'}, axis='columns')

    df_bar_end['Months'] = df_bar_end['Months'].replace(['01'], 'January')
    df_bar_end['Months'] = df_bar_end['Months'].replace(['02'], 'February')
    df_bar_end['Months'] = df_bar_end['Months'].replace(['03'], 'March')
    df_bar_end['Months'] = df_bar_end['Months'].replace(['04'], 'April')
    df_bar_end['Months'] = df_bar_end['Months'].replace(['05'], 'May')
    df_bar_end['Months'] = df_bar_end['Months'].replace(['06'], 'June')
    df_bar_end['Months'] = df_bar_end['Months'].replace(['07'], 'July')
    df_bar_end['Months'] = df_bar_end['Months'].replace(['08'], 'August')
    df_bar_end['Months'] = df_bar_end['Months'].replace(['09'], 'September')
    df_bar_end['Months'] = df_bar_end['Months'].replace(['10'], 'October')
    df_bar_end['Months'] = df_bar_end['Months'].replace(['11'], 'November')
    df_bar_end['Months'] = df_bar_end['Months'].replace(['12'], 'December')

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8,7))

    g = sns.barplot(x='Years',
                    y='Average Page Views',
                    hue='Months',
                    palette=['darkblue', 'orange', 'green', 'red', 'blueviolet', 'brown', 'violet', 'gray', 'olive', 'turquoise', 'royalblue', 'darkorange'],
                    hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                    data=df_bar_end)

    g.set_xticklabels(g.get_xticklabels(), rotation=90)
    plt.legend(loc='upper left', title='Months', fontsize=9.7)




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [x[:4] for x in df_box['date']]
    df_box['Month'] = [x[5:7] for x in df_box['date']]
    df_box = df_box.rename({'value': 'Page Views'}, axis='columns')

    df_box['Month'] = df_box['Month'].replace(['01'], 'Jan')
    df_box['Month'] = df_box['Month'].replace(['02'], 'Feb')
    df_box['Month'] = df_box['Month'].replace(['03'], 'Mar')
    df_box['Month'] = df_box['Month'].replace(['04'], 'Apr')
    df_box['Month'] = df_box['Month'].replace(['05'], 'May')
    df_box['Month'] = df_box['Month'].replace(['06'], 'Jun')
    df_box['Month'] = df_box['Month'].replace(['07'], 'Jul')
    df_box['Month'] = df_box['Month'].replace(['08'], 'Aug')
    df_box['Month'] = df_box['Month'].replace(['09'], 'Sep')
    df_box['Month'] = df_box['Month'].replace(['10'], 'Oct')
    df_box['Month'] = df_box['Month'].replace(['11'], 'Nov')
    df_box['Month'] = df_box['Month'].replace(['12'], 'Dec')

    # Draw box plots (using Seaborn)
    plt.rcParams["figure.figsize"] = [10, 4.5]
    plt.rcParams["figure.autolayout"] = True

    fig, axes = plt.subplots(1, 2)

    g = sns.boxplot(x='Year',
                    y='Page Views',
                    ax=axes[0],
                    data=df_box).set(title='Year-wise Box Plot (Trend)')

    c = sns.boxplot(x='Month',
                    y='Page Views',
                    ax=axes[1],
                    order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    data=df_box).set(title='Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
