import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme('paper')

#https://walker-data.com/geog30323/05-multivariate-visualization.html
#sns.color_palette("flare")

def pieChart(
        counts,
        labels,
        title
        ):
    explode = [0.075, 0]

    plt.pie(
        counts,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
        )

    plt.title(title)
    plt.show()

def showChartComparison(
        playerDicts, 
        chartTitle, 
        chartyLabel, 
        chartxLabel, 
        chartData
        ):
    for player in playerDicts:
        plt.ylabel(chartyLabel)
        plt.xlabel(chartxLabel)
        plt.plot(player[chartData], label=player['strat'])
    plt.title(f'{chartTitle}')
    plt.legend()
    plt.show()

def barCharts(
        playerDicts, 
        chartTitle, 
        chartyLabel, 
        chartxLabel, 
        chartData
        ):
    barGroupYsize=[]
    labels = []
    plt.title(chartTitle)
    plt.xlabel(chartxLabel)
    plt.ylabel(chartyLabel)

    for player in playerDicts:
        labels.append(player['strat'])
        bar = plt.bar(player['strat'], player[chartData], label=player['strat'])
        plt.bar_label(bar, padding=1.5)
        barGroupYsize.append(player[chartData])

    plt.ylim([0, max(barGroupYsize)*1.2])
    plt.xticks(labels, rotation=30, horizontalalignment='right')
    plt.show()

def groupedBarCharts(
        playerDicts,
        labels,
        labelsData, 
        chartTitle, 
        chartyLabel, 
        chartxLabel
        ):
    
    '''
    # Example of data to be passed into function
    groupedBarCharts(
        players,
        ['Highest Bankroll', 'Lowest Bankroll'],
        [
            [player['highest'] for player in players],
            [player['lowest'] for player in players]
        ],
        'Strategy Bankroll Comparison',
        'Amount',
        ''
    )
    '''
    # Grouped bar chart comparisons
    barGroupYsize = []
    groupbars = {}
    width = 0.15
    multiplier = 0
    arangelabels = np.arange(len(labels))
    multiplier = 0
    zippedData= zip(*labelsData)
    
    for player in playerDicts:
        groupbars[player['strat']] = list(next(zippedData))
    
    for k,v in groupbars.items():
        offset = width * multiplier
        bar = plt.bar(arangelabels + offset, v, width, label=k)
        plt.bar_label(bar, padding=3, rotation='vertical')
        multiplier += 1

    # y axis ending parameters
    for k, v in groupbars.items():
        barGroupYsize = barGroupYsize + v

    # Labels
    plt.ylabel(chartyLabel)
    plt.xlabel(chartxLabel)
    plt.title(chartTitle)
    plt.ylim([0, max(barGroupYsize)*1.2])
    # Valid font size are xx-small, x-small, small, medium, large, x-large, xx-large, larger, smaller, None
    # Legend location: supported values are 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
    #plt.legend(loc='upper center', ncol=len(labels), fontsize='small')
    plt.legend(bbox_to_anchor=(0.5, 1.24), ncol=len(labels), loc='upper center')
    plt.xticks(arangelabels+width*(len(labels)/2), labels, rotation=30, horizontalalignment='right')
    plt.show()
    