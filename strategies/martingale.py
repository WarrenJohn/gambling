from random import randint, uniform
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import graphing as g
from players import playerflat, playermg, playerrandom
from strategies import flatbet, randomBet, martingale
sns.color_palette('rocket')
# Axes labels
#plt.tick_params(right=True, top=True, labelright=True, labeltop=True, labelrotation=0)

# Deep diving into the Martingale Strategy

# Analyze:
# How often strat goes bust?
# How much money it makes?
# Is it risky?
## Can it make money??
## Performance with different house edges (Expected Value), bankroll and unit sizes
## Largest bets & their consistency of appearance (RISK)
## Largest bankroll achieved (RETURN ON RISK)
## How long did they last on average (LIFESPAN)
## Number of times player went bankrupt (RISK OF RUIN)
## Number of times player won
## Does the strategy compare with, or beat flat betting and random betting

players = [playerflat, playermg]
simulationsconst = 20
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
    bankroll = 200
    unit = 1
    bet = unit
    spinsconst = 100
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
        # Random Bet Size
        #playerrandom = randomBet(roundWon, playerrandom, [1,bankroll*.15])
        # Martingale
        playermg = martingale(roundWon, playermg) 

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
        
        #####
        # Showing the survival rate,
        # Record each simulation that the player wins and 
        # divide it by the number of over all simulations
        # Can be easily displayed in a pie graph or something
        #####
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
    labels = [f'Win\n{len(win)}', f'Lose\n{len(lose)}'],
    #pieColors = ['green','red'],
    title = f'Win/Loss Ratio (Expected Value: {edge}%)',
    colors='muted'
)

# Bet density distribution
sns.displot(
    roundResults, 
    x='Bet', 
    hue='Strategy', 
    kind='kde',
    palette='Set1',
    cut=0, # Prevents smoothing of data showing unrealistic values
    fill=True).set(
        title=f'Bet Density Distribution (Expected Value: {edge}%)'
        )
plt.tight_layout()
plt.show()

# Bankroll density distribution
sns.displot(
    roundResults, 
    x='Bankroll', 
    hue='Strategy', 
    kind='kde',
    palette='Set1',
    cut=0, # Prevents smoothing of data showing unrealistic values
    fill=True).set(
        title=f'Bankroll Density Distribution (Expected Value: {edge}%)'
        )
plt.tight_layout()
plt.show()

# Lifespan Comparison by simulation
sns.catplot(
    data=simResults,
    x='Simulation',
    y='Lifespan', 
    hue='Strategy',
    kind='point',
    palette='Set1',
    ).set(title=f'Lifespan Comparison (Expected Value: {edge}%)')
#plt.legend(loc='center right', bbox_to_anchor=(1.32, 0.5), ncol=1)
plt.tight_layout()
plt.show()

# Highest Bankroll achieved
sns.violinplot(
    data=simResults,
    y='Highest Bankroll',
    hue='Strategy',
    palette='Set2'
    ).set(title=f'Highest Bankroll Reached (Expected Value: {edge}%)')
plt.tight_layout()
plt.show()

'''
# Hard to read, replaced with a violinplot
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
    ).set(title=f'Highest Bankroll Reached (Expected Value: {edge}%)')
plt.legend(loc='center right', bbox_to_anchor=(1.32, 0.5), ncol=1)
plt.show()
'''
# Lowest Bankroll Achieved
sns.violinplot(
    data=simResults,
    y='Lowest Bankroll',
    hue='Strategy',
    palette='Set2'
    ).set(title=f'Lowest Bankroll Reached (Expected Value: {edge}%)')
plt.tight_layout()
plt.show()

'''
# Hard to read, replaced with a violinplot
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
    ).set(title=f'Lowest Bankroll Reached relative to Lifespan (size) (Expected Value: {edge}%)')
plt.legend(loc='center right', bbox_to_anchor=(1.32, 0.5), ncol=1)
plt.show()
'''

# Bet Sizes Line plot
sns.relplot(
    data=roundResults, kind='line',
    #x=roundResults.index # Previous x axis
    x='Round', y='Bet',
    hue='Simulation', 
    style='Strategy',
    palette='flare',
    #height=5,
    aspect=1.4
).set(title=f'Bet history throughout all simulations (Expected Value: {edge}%)')
plt.show()

# Bankroll History Line plot
sns.relplot(
    data=roundResults, kind='line',
    x='Round', y="Bankroll",
    hue='Simulation',
    style='Strategy',
    palette='hls',
    #height=5,
    aspect=1.5
).set(title=f'Bankroll history throughout all simulations (Expected Value: {edge}%)')
#plt.tick_params(right=True, labelright=True)
plt.show()
