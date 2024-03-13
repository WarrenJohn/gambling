from random import randint
import matplotlib.pyplot as plt
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
edge = 49
edge = edge+1
bankroll = 10000
unit = 1
bet = unit
spins = 50000
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
fig, ax = plt.subplots()

labels = [f'Win {len(win)}', f'Lose {len(lose)}']
counts = [len(win), len(lose)]
bar_colors = ['green','red']

ax.bar(labels, counts, color=bar_colors)

ax.set_ylabel('Occurances')
ax.set_title('Results')
plt.show()

# Players highest Balance

fig, ax = plt.subplots()

labels = []
counts = []
colors = []

for player in players:
    labels.append(f'{player["strat"]} ${player["highest"]}')
    counts.append(player['highest'])
    colors.append(player['graphcolor'])

ax.barh(labels, counts, color=colors)

ax.set_ylabel('Amount')
ax.set_title('Highest Bankroll Achieved')
plt.show()

# Charts
plt.title('Flat Betting')
# Axes labels
plt.ylabel('Bankroll')
plt.xlabel('Spins')
# y axis start ending parameters
#plt.ylim([0, max(ysizeMax)*1.2])
# Data
plt.plot(playerflat['history'], color='orange', label='Flat Bet')
plt.show()

plt.title('Negative Progressions')
# Axes labels
plt.ylabel('Bankroll')
plt.xlabel('Spins')
# y axis start ending parameters
plt.ylim([0, max(ysizeMax)*1.2])
# Data
plt.plot(playermg['history'], color=playermg['graphcolor'], label=playermg['strat'])
plt.plot(playergmg['history'],color=playergmg['graphcolor'], label=playergmg['strat'])
plt.plot(playerlab['history'], color=playerlab['graphcolor'], label=playerlab['strat'])
plt.legend()
plt.show()
'''
plt.title('Labouchere')
# Axes labels
plt.ylabel('Bankroll')
plt.xlabel('Spins')
# y axis start ending parameters
plt.ylim([0, max(ysizeMax)*1.2])
# Data
plt.plot(playerlab['history'], color=playerlab['graphcolor'], label=playerlab['strat'])
plt.show()
'''