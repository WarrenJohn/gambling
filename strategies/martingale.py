from random import randint, uniform
import matplotlib.pyplot as plt
import graphing as g
from players import playerflat, playermg, playerrandom
from strategies import flatbet, randomBet, martingale

# Deep diving into the Martingale Strategy

# Analyze:
## Can it make money??
## Performance with different house edges, bankroll and unit sizes
## Largest bets & their consistency of appearance (RISK)
## How long did they last on average (LIFESPAN)
## Number of times player went bankrupt (RISK OF RUIN)
## Number of times player won
## Does the strategy compare with, or beat flat betting and random betting

simulationsconst = 1
simulations = simulationsconst

while simulations > 0:
    simulations -= 1
    # Player variables
    houseEdge = 1.24
    edge = 50 - houseEdge
    bankroll = 2000
    unit = 1
    bet = unit
    spinsconst = 1000
    spins = spinsconst
    sequence = [1,1]
    players = [playerflat, playerrandom, playermg]

    # Graphing variables
    spinsMade = 0
    results = []
    win = []
    lose = []

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
        
    # Running each strategy
    while spins > 0:
        results.append(round(uniform(1,100), 2))
        spins -= 1

    for number in results:
        roundWon = number < edge
        spinsMade += 1
        if roundWon:
            win.append(number)
        else:
            lose.append(number)
        # Flat Betting
        playerflat = flatbet(roundWon, playerflat)
        # Random Bet Size
        playerrandom = randomBet(roundWon, playerrandom, [1,bankroll*.035])
        # Martingale
        playermg = martingale(roundWon, playermg)

    # Getting the largest value for the graph
    for player in players:
        player['highest'] = max(player['history'])
        player['lowest'] = min(player['history'])

    # Wins/Losses pie chart
    #Included to double check edge is working correctly

    g.pieChart(
        counts = [(len(win)/spinsconst)*100, (len(lose)/spinsconst)*100],
        labels = [f'Win {len(win)}', f'Lose {len(lose)}'],
        pieColors = ['green','red'],
        title = 'Results'
    )

    # Grouped bar chart comparisons
    g.groupedBarCharts(
        players,
        [
            'Highest Bankroll',
            'Lowest Bankroll',
            'Largest Bet',
            'Smallest Bet',
            'Next Bet'
         ],
        [
            [player['highest'] for player in players],
            [player['lowest'] for player in players],
            [max(player['bethistory']) for player in players],
            [min(player['bethistory']) for player in players],
            [player['bet'] for player in players]
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

    # Bet History Chart
    g.showChartComparison(
        players,
        'Bet sizes over time',
        'Bet size',
        'Rounds',
        'bethistory'
    )
    # Show all strategies individually

    for player in players:
        plt.title(player['strat'])
        plt.ylabel('Bankroll')
        plt.xlabel('Spins')
        plt.plot(player['history'], label=player['strat'])
        plt.show()
