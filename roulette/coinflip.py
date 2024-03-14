from random import randint
import matplotlib.pyplot as plt
import numpy as np
from players import playerflat, playermg, playergmg, playerlab
from strategies import flatbet, martingale, grandmartingale, labouchere

# This is just a simple weighted coing flip program to test strategies
# You can change the house edge via the edge variable and test the strategies to mimic different casino games

# Player variable descriptions
#edge = 49 # 51 is 1% in favor of the player, 49 is 1% in favor of the casino
#edge = edge+1 # range() checks up to the last number, not including
#bankroll = x # starting money
#unit = x # base bet size
#bet = unit # current / running bet size
#spins = x # simulation length

# Player variables
edge = 50
edge = edge+1
bankroll = 10000
unit = 1
bet = unit
spinsconst = 50000
spins = spinsconst
sequence = [1, 2, 2, 3, 1, 1]
players = [playerflat, playermg, playergmg, playerlab]

# Graphing variables
spinsMade = 0
results = []
win = []
lose = []
ysizeMax = []
ysizeMin = []

# Holds players betting strategies
'''
# Example of a players dict
playerflat = {
    'strat': 'Flat Betting',
    'startingbankroll': 0,
    'bankroll':0,
    'bet': 0,
    'betsequence': [],
    'betprogression': [],
    'bethistory': [],
    'unit': 0,
    'history': [],
    'highest': 0,
    'spinscompleted': 0,
    'graphcolor': 'orange'
}
'''
# Assigning & resetting player values
# If not reset, values are stored in cache,
# and will appear on the graph in the next simulation

for player in players:
    player.update({
        'startingbankroll': bankroll,
        'bankroll': bankroll,
        'bet': unit,
        'betsequence': sequence[:],
        'betprogression': sequence[:],
        'unit': unit,
        'history': [],
        'highest': 0,
        'spinscompleted': 0
        })

playerlab['bet'] = playerlab['betprogression'][0] + playerlab['betprogression'][-1]

# Running each strategy
while spins > 0:
    results.append(randint(1,100))
    spins -= 1

for number in results:
    roundWon = number in range(1, edge)
    spinsMade += 1
    if roundWon:
        win.append(number)
    else:
        lose.append(number)
    # Flat Betting
    playerflat = flatbet(roundWon, playerflat)
    # Martingale
    playermg = martingale(roundWon, playermg)
    # Grand Martingale
    playergmg = grandmartingale(roundWon, playergmg)
    # Labouchere
    playerlab = labouchere(roundWon, playerlab, sequence)


# Getting the largest value for the graph
for player in players:
    ysizeMax.append(max(player['history']))
    #ysizeMin.append(min(player['history']))
    player['highest'] = max(player['history'])


# Wins/Losses bar graph
#Included to double check edge is working correctly
labels = [f'Win {len(win)}', f'Lose {len(lose)}']
counts = [(len(win)/spinsconst)*100, (len(lose)/spinsconst)*100]
explode = [0.1, 0]
pie_colors = ['green','red']

plt.pie(
    counts,
    explode=explode,
    labels=labels,
    autopct='%1.1f%%',
    shadow=True,
    startangle=90,
    colors=pie_colors
    )

#plt.ylabel('Occurances')
plt.title('Results')
plt.show()

# Grouped bar chart comparisons
labels = []
groupbarlegend = []
groupbars = {
    'Highest Bankroll' : [],
    'Highest Bet' : [],
    'Lifespan': []
}
# Data
for player in players:
    groupbarlegend.append(player['strat'])
    groupbars['Highest Bankroll'].append(player['highest'])
    groupbars['Lifespan'].append(player['spinscompleted'])
    groupbars['Highest Bet'].append(max(player['bethistory']))
    labels.append(player['strat'])

width = 0.2
multiplier = 0
arangelabels = np.arange(len(labels))
multiplier = 0

for k,v in groupbars.items():
    offset = width * multiplier
    bar = plt.bar(arangelabels + offset, v, width, label=k)
    plt.bar_label(bar, padding=3, rotation='vertical')
    multiplier += 1

# y axis ending parameters
ySizeMax = max(groupbars['Lifespan'])
plt.ylim([0, ySizeMax*1.2])

# Labels
plt.ylabel('Amount')
plt.xlabel('Strategy')
plt.title('Strategy Comparison')
plt.legend()
plt.xticks(arangelabels+width, labels)
plt.show()

# Negative Progression Charts
plt.title('Negative Progressions')
# Axes labels
plt.ylabel('Bankroll')
plt.xlabel('Spins')
# Data
plt.plot(playermg['history'], color=playermg['graphcolor'], label=playermg['strat'])
plt.plot(playergmg['history'],color=playergmg['graphcolor'], label=playergmg['strat'])
plt.plot(playerlab['history'], color=playerlab['graphcolor'], label=playerlab['strat'])
plt.legend()
plt.show()

# Show all strategies individually

for player in players:
    plt.title(player['strat'])
    plt.ylabel('Bankroll')
    plt.xlabel('Spins')
    plt.plot(player['history'], color=player['graphcolor'], label=player['strat'])
    plt.show()
