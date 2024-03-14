'''
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
    'spinscompleted': 0,
    'graphcolor': 'orange'
}
'''

def updatePlayerDict(playerDict):
    # Updates all necesary information to the player dictionary
    # for the purposes of graphing and data tracking
    playerDict['history'].append(playerDict['bankroll'])
    playerDict['bethistory'].append(playerDict['bet'])
    playerDict['spinscompleted'] += 1
    return playerDict