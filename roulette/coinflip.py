from random import randint
import matplotlib.pyplot as plt
import numpy as np
import graphing as g
from players import playerflat, playermg, playergmg, playerlab, playerparoli
from strategies import flatbet, martingale, grandmartingale, labouchere, paroli

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
edge = 49
edge = edge+1
bankroll = 200
unit = 1
bet = unit
spinsconst = 500
spins = spinsconst
sequence = [1, 2, 2, 3, 1, 1]
posprogplayers = [playerflat, playerparoli]
negprogplayers = [playermg, playergmg, playerlab]
players = posprogplayers + negprogplayers

# Graphing variables
spinsMade = 0
results = []
win = []
lose = []

# Holds players betting strategies
'''
# Example of a players dict
playerflat = {
    'strat': 'Flat Betting',
    'startingbankroll': 0,
    'bankroll':0,
    'bet': 0,
    'betsequence': [], # bet sequence to be used for betprogression
    'betprogression': [], # current betting progression in use (ex. labouchere)
    'bethistory': [],
    'unit': 0,
    'history': [], # bankroll history
    'highest': 0, # highest bankroll
    'lowest': 0, # lowest bankroll
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
        'bethistory': [],
        'unit': unit,
        'history': [],
        'highest': 0,
        'lowest': 0,
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
    # Paroli
    playerparoli = paroli(roundWon, playerparoli)

# Getting the largest value for the graph
for player in players:
    player['highest'] = max(player['history'])
    player['lowest'] = min(player['history'])

# Wins/Losses pie chart
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
g.groupedBarCharts(
    players,
    ['Highest Bankroll', 'Lowest Bankroll', 'Max Bet Size', 'Min Bet Size', 'Last Bet Size', 'Spins Completed'],
    [
        [player['highest'] for player in players],
        [player['lowest'] for player in players],
        [max(player['bethistory']) for player in players],
        [min(player['bethistory']) for player in players],
        [player['bet'] for player in players],
        [player['spinscompleted'] for player in players]
    ],
    'Strategy Bankroll Comparison',
    'Amount',
    ''
)

# Lifespan bar chart
g.barCharts(
    players,
    'Lifespan',
    'Rounds',
    'Strategy',
    'spinscompleted'
)

# Negative Progression Bet History Chart
g.showChartComparison(
    negprogplayers,
    'Negative Progression Bet Sizes',
    'Bet size',
    'Rounds',
    'bethistory'
)

# Positive Progression Bet History Chart
'''
g.showChartComparison(
    posprogplayers,
    'Positive Progression Bet Sizes',
    'Bet size',
    'Rounds',
    'bethistory'
    )
'''

# Negative Progression Charts
g.showChartComparison(
    negprogplayers,
    'Negative Progressions',
    'Bankroll',
    'Rounds',
    'history'
    )

# Show all strategies individually

for player in players:
    plt.title(player['strat'])
    plt.ylabel('Bankroll')
    plt.xlabel('Spins')
    plt.plot(player['history'], color=player['graphcolor'], label=player['strat'])
    plt.show()
