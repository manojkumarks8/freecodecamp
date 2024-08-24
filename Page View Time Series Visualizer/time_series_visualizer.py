import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


file_path = 'fcc-forum-pageviews.csv'
df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')
df.head(), df.describe()
df_cleaned = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    plt.figure(figsize=(15, 6))
    plt.plot(df_cleaned.index, df_cleaned['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig = plt.gcf()
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    df_bar = df_cleaned.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_pivot = df_bar.pivot_table(values='value', index='year', columns='month', aggfunc='mean').fillna(0)
    df_pivot = df_pivot[['January', 'February', 'March', 'April', 'May', 'June', 'July',
                         'August', 'September', 'October', 'November', 'December']]


    df_pivot.plot(kind='bar', figsize=(15, 8))
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    fig = plt.gcf()
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    df_box = df_cleaned.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    fig.savefig('box_plot.png')
    return fig


line_fig = draw_line_plot()
bar_fig = draw_bar_plot()
box_fig = draw_box_plot()
line_fig, bar_fig, box_fig
