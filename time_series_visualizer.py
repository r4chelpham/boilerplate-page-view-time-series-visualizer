import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = ['date'], parse_dates = ['date'])

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025))
        & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plotpip 

    fig, axes = plt.subplots(figsize = (13,9))

    axes = sns.lineplot(data=df, x="date", y="value")

    axes.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')

    axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]
    df_bar['average'] = df_bar.groupby(by = ['year', 'month'])['value'].transform('mean')
    df_bar = df_bar[['year', 'month', 'average']].drop_duplicates(keep='first')

    print(df_bar)

    # Draw bar plot

    fig, axes = plt.subplots(figsize=(16,9))

    sns.barplot(data=df_bar, x='year', y='average', hue='month',
                order=[2016, 2017, 2018, 2019], hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(loc=2, title='Months')
  
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]


    # Draw box plots (using Seaborn)

    fig, (axes1, axes2) = plt.subplots(1, 2, figsize=(16, 9))

    sns.boxplot(data=df_box, x=df_box['year'], y=df_box['value'], ax=axes1)
  
    axes1.set_xlabel("Year")
    axes1.set_ylabel("Page Views")
    axes1.set_title("Year-wise Box Plot (Trend)")
  
    sns.boxplot(data=df_box, 
                x=df_box['month'], 
                y=df_box['value'], 
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
                ax=axes2)
  
    axes2.set_xlabel("Month")
    axes2.set_ylabel("Page Views")
    axes2.set_title("Month-wise Box Plot (Seasonality)")
  
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
