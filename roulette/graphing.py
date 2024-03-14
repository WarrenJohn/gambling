#import roulette as r
#from strategies import flatbet
#from betwon import betwon
import matplotlib.pyplot as plt
import numpy as np

def showChartComparison(playerDicts, chartTitle, chartyLabel, chartxLabel, chartData):
    for player in playerDicts:
        plt.ylabel(chartyLabel)
        plt.xlabel(chartxLabel)
        plt.plot(player[chartData], color=player['graphcolor'], label=player['strat'])
    plt.title(f'{chartTitle}')
    plt.legend()
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