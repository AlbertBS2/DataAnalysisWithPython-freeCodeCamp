import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
BMI = df["weight"] / ((df["height"])/100)**2
df['overweight'] = BMI
df.loc[df["overweight"] <= 25, "overweight"] = 0
df.loc[df["overweight"] > 25, "overweight"] = 1


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df["cholesterol"] <= 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1

df.loc[df["gluc"] <= 1, "gluc"] = 0
df.loc[df["gluc"] > 1, "gluc"] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], id_vars=['cardio'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat['value'] = df_cat['value'].astype(int)
    df_cat = df_cat.sort_values('variable')

    # Draw the catplot with 'sns.catplot()'
    sns.set_theme(style="ticks")

    # Get the figure for the output
    fig = sns.catplot(x="variable",
                      col='cardio',
                      hue='value',
                      kind='count',
                      data=df_cat)
    fig = fig.set(ylabel='total').fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.copy()

    df_heat.loc[df["ap_lo"] > df_heat['ap_hi'], "ap_lo"] = np.nan

    df_heat.loc[df['height'] < df['height'].quantile(0.025), 'height'] = np.nan
    df_heat.loc[df['height'] > df['height'].quantile(0.975), 'height'] = np.nan

    df_heat.loc[df['weight'] < df['weight'].quantile(0.025), 'weight'] = np.nan
    df_heat.loc[df['weight'] > df['weight'].quantile(0.975), 'weight'] = np.nan

    df_heat.dropna(inplace=True)

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr,
                     mask=mask,
                     square=True,
                     center=0,
                     vmin=-0.15,
                     vmax=0.30,
                     annot=True,
                     linewidths=0.7,
                     cbar_kws={'fraction': 0.024, 'ticks': [-0.08, 0.00, 0.08, 0.16, 0.24]},
                     fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig