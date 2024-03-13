
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

playermg = {
    'strat': 'Martingale',
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
    'graphcolor': 'red'
}

playergmg = {
    'strat': 'Grand Martingale',
    'startingbankroll': 0,
    'bankroll':0,
    'bet': 0,
    'betsequence': [], # bet sequence to be used for betprogression
    'betprogression': [], # current betting progression in use (ex. labouchere)
    'bethistory': [],
    'unit': 0,
    'history': [], # bankroll history
    'highest': 0, # highest bet
    'spinscompleted': 0,
    'graphcolor': 'blue'
}

playerlab = {
    'strat': 'Labouchere',
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
    'graphcolor': 'green'
}

players = [playerflat, playermg, playergmg, playerlab]