import roulette as r
from roulette.strategies import flatbet
from betwon import betwon
import matplotlib.pyplot as plt



#Grand Martingale Betting
'''
playerbet = 'red'
spins = 10000000
spinsMade = 0
betsize = 1
currentbet = 1
bankroll = 500000
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
        if betwon(playerbet, result):
            bankroll += currentbet
            currentbet = betsize
        else:
            bankroll -= currentbet
            currentbet *= 2
            currentbet +=betsize
        if currentbet > bankroll:
            break
        betSizeHistory.append(currentbet)
        playerHistory.append(result)
        wheelResults.append(result)
        bankrollHistory.append(bankroll)
    else:
        break

plt.plot(betSizeHistory)
'''
'''
# Martingale Betting

playerbet = 'red'
spins = 100000
spinsMade = 0
betsize = 1
currentbet = 1
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
        if betwon(playerbet, result):
            bankroll += currentbet
            currentbet = betsize
        else:
            bankroll -= currentbet
            currentbet *= 2
        if currentbet > bankroll:
            break
        betSizeHistory.append(currentbet)
        playerHistory.append(result)
        wheelResults.append(result)
        bankrollHistory.append(bankroll)
    else:
        break

plt.plot(betSizeHistory)
'''

'''
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
#Line Chart

plt.plot(bankrollHistory)
plt.ylabel('Bankroll over time')
plt.xlabel('Spins')
plt.ylim([0, max(bankrollHistory)*1.05])

#Horizontal Bar Graph

resultsColors, red, black, green = r.getColors(wheelResults)
resultsOddEven, odd, even = r.getOddEven(wheelResults)
fig, ax = plt.subplots()
results = [f'Red\n({red})', f'Black\n({black})', f'Green\n({green})', f'Odd\n({odd})', f'Even\n({even})']
counts = [red, black, green, odd, even]
bar_colors = ['red', 'black', 'green', 'grey', 'blue']


#bar graph values
#for i, v in enumerate(counts):
#    ax.text(v + 3, i + .25, str(v), 
#            color = 'black', fontweight = 'bold')

ax.barh(results, counts, color=bar_colors)

ax.set_ylabel('# Occurances')
ax.set_title('Roulette spin Results')

plt.show()
'''