
playerflat = {
    'strat': 'Flat Betting'
}

playermg = {
    'strat': 'Martingale'
}

playergmg = {
    'strat': 'Grand Martingale'
}

playerlab = {
    'strat': 'Labouchere'
}

playerparoli = {
    'strat': 'Paroli'
}

playerrandom = {
    'strat': 'Random'
}
players = [
    playerflat, 
    playermg, 
    playergmg, 
    playerlab, 
    playerparoli, 
    playerrandom
    ]

for player in players:
    player.update({
    'startingbankroll': 0,
    'bankroll':0,
    'bank': 0, # players bank acct, money removed from bankroll and transferred into bank (not available for gambling)
    'bet': 0,
    'winlose':[],
    'tablemin': 0,
    'tablemax': 0,
    'betsequence': [], # bet sequence to be used for betprogression
    'betprogression': [], # current betting progression in use (ex. labouchere)
    'bethistory': [],
    'unit': 0,
    'history': [], # bankroll history
    'highest': 0, # highest bankroll
    'lowest': 0, # lowest bankroll
    'spinscompleted': 0,
    'survived': [] # for checking the survival rate of simulations
    })