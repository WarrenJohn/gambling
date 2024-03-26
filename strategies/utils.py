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

def updatePlayerDict(betwon, playerDict):
    # Updates all necesary information to the player dictionary
    ## for the purposes of graphing and data tracking
    # Last bet added to the bethistory
    # Bankroll reduced or increased by last item in bethistory
    # Bankroll updated in history list after modification to reflect result
    # Next bet is calculated by parent function
    playerDict['spinscompleted'] += 1
    playerDict['winlose'].append(betwon)
    playerDict['bethistory'].append(playerDict['bet'])
    if betwon:
        playerDict['bankroll'] += playerDict['bethistory'][-1]
    else:
        playerDict['bankroll'] -= playerDict['bethistory'][-1]
    playerDict['history'].append(playerDict['bankroll']) # appended last to reflect the results of the last round
    return playerDict