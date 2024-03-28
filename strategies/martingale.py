from random import uniform
from itertools import groupby
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from players import playerflat, playermg
from strategies import flatbet, martingale

sns.set_theme('paper')
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
simStreaks = []
streakDict = {
    'win': [],
    'lose': []
}
sortedStreaks = []


while simulations <  simulationsconst:
    roundNum = 0
    simulations += 1
    # Player variables
    edge = -2.70
    gameEdge = 50 + edge
    bankroll = 200
    unit = 1
    bet = unit
    spinsconst = 1000
    spins = 0
    sequence = [1,1]
    streaks = []

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
        # Checking the win/lose streaks for ALL results - not just each player
        streaks.append(roundWon)
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
    simStreaks.append(streaks)
        #####
        # Showing the survival rate,
        # Record each simulation that the player wins and 
        # divide it by the number of over all simulations
        # Can be easily displayed in a pie graph or something
        #####
    ############## SIMULATION COMPLETE ##############


# Sorting winning and losing streaks and preparing for a dataframe
for lst in simStreaks:
    sortedStreaks.append([list(j) for i, j in groupby(lst)])

for lst in sortedStreaks:
    lst[:] = [x for x in lst if len(x)>1]

sortedStreaks[:] = sum(sortedStreaks, [])

for lst in sortedStreaks:
    if lst[0] == True:
        streakDict['win'].append(len(lst))
    else:
        streakDict['lose'].append(len(lst))

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
streakResults = pd.DataFrame(
    dict(
        [
            (key, pd.Series(value)) 
            for key, value in streakDict.items()]
        )
    )
print('win',len(streakDict['win']), 'lose',len(streakDict['lose']))

# Finding info in a dataframe
# Future reference
#roundResults.loc[(roundResults['Strategy'] == 'Martingale')][['Simulation', 'Win/Lose']]
# Also a .groupby() function

# Wins/Losses pie chart
#Included to double check edge is working correctly
plt.pie(
    [(len(win)/spinsconst)*100, (len(lose)/spinsconst)*100],
    #labels = [f'Win\n{len(win)}', f'Lose\n{len(lose)}'],
    autopct='%1.1f%%',
    pctdistance=1.15,
    startangle=90,
    colors=sns.color_palette('muted'),
    textprops={'weight':'bold'}
    )

plt.pie(
    [
        len(streakDict['win'])/(len(streakDict['win'])+len(streakDict['lose']))*100,
        len(streakDict['lose'])/(len(streakDict['win'])+len(streakDict['lose']))*100
    ],
    #labels = [
    #    f'Win Streaks\n{len(streakDict["win"])}', 
    #    f'Loss Streaks\n{len(streakDict["lose"])}'
    #],
    autopct='%1.1f%%',
    pctdistance=0.45,
    colors=sns.color_palette('Accent'),
    radius=0.75,
    startangle=90,
    textprops={'weight':'bold'}
    )

centre_circle = plt.Circle(
    (0,0),
    0.5,color='black', 
    fc='white',
    linewidth=0
    )


plt.legend(labels=[
        f'Win\n{len(win)}',
        f'Lose\n{len(lose)}',
        f'Win Streaks\n{len(streakDict["win"])}', 
        f'Loss Streaks\n{len(streakDict["lose"])}'
    ],
    loc='upper right'
    )

plt.title(f'Win/Loss Ratio \n(Expected Value: {edge}%)')
plt.gcf().gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  
plt.tight_layout()

#plt.savefig(f'winlossratio{edge}.png', bbox_inches='tight')
plt.show()

# Graphing winning and losing streaks by lengths and amount per streak
streakYticks = [[v for v in
    sorted(Counter(streakDict['win']).values())
    ],[v for v in
    sorted(Counter(streakDict['lose']).values())
    ]]

streakXticks = [k for k in 
        Counter(streakDict['win'])|Counter(streakDict['lose'])
        ]


sns.displot(
    streakResults,
    element='step',
)

plt.yscale('log')
plt.yticks(streakYticks[1], streakYticks[1])
plt.ylabel('Number of Streaks')

plt.xticks(streakXticks, streakXticks)
plt.xlabel('Streak Lengths')
plt.title(f'Winning and Losing Streaks (Expected Value: {edge}%)')
plt.tight_layout()
plt.show()

'''
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
#plt.savefig(f'betdensity{edge}.png', bbox_inches='tight')
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
#plt.savefig(f'bankrolldensity{edge}.png', bbox_inches='tight')
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
#plt.savefig(f'lifespan{edge}.png', bbox_inches='tight')
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
#plt.savefig(f'highestbankroll{edge}.png', bbox_inches='tight')
plt.show()

# Lowest Bankroll Achieved
sns.violinplot(
    data=simResults,
    y='Lowest Bankroll',
    hue='Strategy',
    palette='Set2'
    ).set(title=f'Lowest Bankroll Reached (Expected Value: {edge}%)')
plt.tight_layout()
#plt.savefig(f'lowestbankroll{edge}.png', bbox_inches='tight')
plt.show()

# Bet Sizes Line plot
sns.relplot(
    data=roundResults, kind='line',
    #x=roundResults.index # Previous x axis
    x='Round', y='Bet',
    hue='Simulation', 
    style='Strategy',
    palette='flare',
    #height=5,
    aspect=1.5
).set(title=f'Bet history throughout all simulations (Expected Value: {edge}%)')
#plt.savefig(f'bethistory{edge}.png', bbox_inches='tight')
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
#plt.savefig(f'bankrollhist{edge}.png', bbox_inches='tight')
plt.show()
'''