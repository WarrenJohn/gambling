#import roulette as r
#from strategies import flatbet
#from betwon import betwon
import matplotlib.pyplot as plt
import numpy as np

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
        plt.plot(player[chartData], color=player['graphcolor'], label=player['strat'])
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
    width = 0.15
    barGroupYsize=[]
    plt.title(chartTitle)
    plt.xlabel(chartxLabel)
    plt.ylabel(chartyLabel)

    for player in playerDicts:
        bar = plt.bar(player['strat'], player[chartData], width, label=player['strat'])
        plt.bar_label(bar, padding=1.5)
        barGroupYsize.append(player[chartData])

    plt.ylim([0, max(barGroupYsize)*1.2])
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
    #plt.legend(loc='upper center', ncol=len(labels), fontsize='small')
    plt.legend()
    plt.xticks(arangelabels+width, labels)
    plt.show()

'''
# Example of using the roulette file
#Flat betting

playerbet = 'red'
spins = 1000000
spinsMade = 0
betsize = 1
bankroll = 100000
startingBankroll = bankroll
bankrollHistory = []
betSizeHistory = []
wheelResults = []
playerHistory = []

while spins > 0:
    spins -= 1
    if bankroll > 0:
        spinsMade += 1
        result = r.spinWheel()
        bankroll = flatbet(betwon(playerbet, result),bankroll, betsize)
        playerHistory.append(result)
        wheelResults.append(result)
        bankrollHistory.append(bankroll)
    else:
        break

print('Total spins:',spinsMade)
print('Bankroll', bankroll) #testing purposes
print('Bankroll ROI $', bankroll-startingBankroll, '%', bankroll/startingBankroll*100)
#print(len(playerHistory), playerHistory)
'''