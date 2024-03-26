from random import uniform
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import graphing as g
from players import playerflat, playermg, playergmg, playerlab, playerparoli, playerrandom
from strategies import flatbet, martingale, grandmartingale, labouchere, paroli, randomBet

# Can test as many strategies as wanted simultaneously

# Strategy that regresses bet size closer player is to target profit

# How long do streaks last? Winning and Losing.
# On average and the ouliers

#Joe Croupier youtube
# Roulette Grinder

# https://en.wikipedia.org/wiki/Kelly_criterion

# This is just a simple weighted coing flip program to test strategies
# You can change the house edge via the edge variable and test the strategies to mimic different casino games

# Player variable descriptions
#houseEdge = 1.24 # The houses advantage on the bet, will be subtracted from 50
#bankroll = x # starting money
#unit = x # base bet size
#bet = unit # current / running bet size
#spins = x # simulation length
#sequence = [1, 2, 2, 3, 1, 1] # the betting sequence used, i.e Labouchere


# Analyze:
# How often strat goes bust?
# How much money it makes?
# Is it risky?
## Can it make money??
## Performance with different house edges, bankroll and unit sizes
## Largest bets & their consistency of appearance (RISK)
## Largest bankroll achieved (RETURN ON RISK)
## How long did they last on average (LIFESPAN)
## Number of times player went bankrupt (RISK OF RUIN)
## Number of times player won
## Does the strategy compare with, or beat flat betting and random betting

sns.color_palette('rocket')

players = [playerflat, playermg, playergmg, playerlab, playerparoli, playerrandom]
simulationsconst = 10
simulations = 0
roundsData = []
simData = []
mgTestplots= {
    'Bet History': [],
    'Bankroll History': [],
    'Rounds':[]
}
rounds = []
win = []
lose = []

while simulations <  simulationsconst:
    roundNum = 0
    simulations += 1
    # Player variables
    edge = -2.70
    gameEdge = 50 + edge
    bankroll = 2000
    unit = 1
    bet = unit
    spinsconst = 1000
    spins = 0
    sequence = [1,1]

    # Graphing variables
    spinsMade = 0
    results = []
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
            'spinscompleted': 0,
            'survived':[]
            })
        
    # Running each strategy
    while spins < spinsconst:
        results.append(round(uniform(1,100), 2))
        spins += 1

    for number in results:
        roundNum += 1
        roundWon = number < gameEdge
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
        # Random Bet Size
        playerrandom = randomBet(roundWon, playerrandom, [1,10])

        for player in players:
            roundsData.append(
                    [
                        simulations,
                        roundNum, 
                        player['strat'],
                        player['bankroll'],
                        player['bet'],
                        roundWon,
                        edge
                    ]
                )
    

    # Getting the largest value for the graph
    for player in players:
        player['highest'] = max(player['history'])
        player['lowest'] = min(player['history'])
        player['survived'] = len(player['history'])>=spinsMade
        simData.append(
            [
            simulations,
            player['strat'],
            player['highest'],
            player['lowest'],
            max(player['bethistory']),
            min(player['bethistory']),
            player['spinscompleted'],
            edge
            ]
            )
    ############## SIMULATION COMPLETE ##############

roundResults = pd.DataFrame(
    roundsData, 
    columns=
    [
        'Simulation',
        'Round',
        'Strategy', 
        'Bankroll',
        'Bet',
        'Win/Lose',
        'Edge'
    ]
)  

simResults = pd.DataFrame(simData, columns=
        [
            'Simulation',
            'Strategy',
            'Highest Bankroll',
            'Lowest Bankroll', 
            'Highest Bet',
            'Lowest Bet',
            'Lifespan',
            'Edge'
        ]
    )

# Wins/Losses pie chart
#Included to double check edge is working correctly

g.pieChart(
    counts = [(len(win)/spinsconst)*100, (len(lose)/spinsconst)*100],
    labels = [f'Win {len(win)}', f'Lose {len(lose)}'],
    #pieColors = ['green','red'],
    title = 'Results'
)


# Bet density distribution
sns.displot(roundResults, x='Bet', hue="Strategy", kind="kde", fill=True).set(title='Bet Density Distribution')
plt.show()

# Bankroll density distribution
sns.displot(roundResults, x='Bankroll', hue="Strategy", kind="kde", fill=True).set(title='Bankroll Density Distribution')
plt.show()

# Lifespan Comparison by simulation
sns.barplot(
    data=simResults,
    x="Simulation", 
    y="Lifespan", 
    hue="Strategy",
    palette='rocket',
    ).set(title='Lifespan Comparison')
plt.legend(loc='center right', bbox_to_anchor=(1.32, 0.5), ncol=1)
plt.show()

# Highest Bankroll achieved
sns.scatterplot(
    data=simResults, 
    x='Simulation',
    y='Highest Bankroll',
    size='Lifespan',
    hue='Strategy',
    sizes=(40, 250),
    palette='rocket'
    #errorbar="sd", 
    #palette='dark', 
    #alpha=.6
    ).set(title='Highest Bankroll Reached relative to Lifespan(size)')
plt.legend(loc='center right', bbox_to_anchor=(1.32, 0.5), ncol=1)
plt.show()

# Lowest Bankroll Achieved
sns.scatterplot(
    data=simResults, 
    x= 'Simulation',
    y='Lowest Bankroll', 
    hue='Strategy',
    size='Lowest Bankroll',
    sizes=(40, 250),
    palette='rocket'
    #palette='dark', 
    #alpha=.6
    ).set(title='Lowest Bankroll Reached relative to Lifespan (size)')
plt.legend(loc='center right', bbox_to_anchor=(1.32, 0.5), ncol=1)
plt.show()

sns.relplot(
    data=roundResults, kind='line',
    x=roundResults.index, y='Bet',
    hue='Simulation', 
    style='Strategy',
    #height=5,
    aspect=1.4
).set(title='Largest Bet sizes throughout all simulations')
plt.show()

sns.relplot(
    data=roundResults, kind='line',
    x='Round', y="Bankroll",
    hue='Simulation', 
    style='Strategy',
    #height=5,
    aspect=1.4
).set(title='Bankroll history throughout all simulations')
plt.show()