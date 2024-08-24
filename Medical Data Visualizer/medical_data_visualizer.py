import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data
df = pd.read_csv('medical_examination.csv')

# 2. Calculate BMI and add 'overweight' column
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)
df.drop(columns=['BMI'], inplace=True)

# 3. Normalize cholesterol and gluc columns
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw the Categorical Plot
def draw_cat_plot():
    # Load the data
    df = pd.read_csv('medical_examination.csv')

    # Add 'overweight' column
    df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)

    # Normalize cholesterol and gluc values
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
    df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

    # Convert data to long format
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to calculate counts
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Draw the catplot
    fig = sns.catplot(
        x="variable", y="total", hue="value", col="cardio",
        data=df_cat, kind="bar", height=6, aspect=1
    ).fig

    # Save the plot
    fig.savefig('catplot.png')
    return fig

# 10. Draw the Heat Map
def draw_heat_map():
    # 11. Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12. Calculate the correlation matrix
    corr = df_heat.corr()

    # 13. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15. Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", ax=ax, cmap='coolwarm', center=0)

    # 16. Save the heatmap and return the figure
    fig.savefig('heatmap.png')
    return fig
