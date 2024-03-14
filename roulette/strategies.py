from utils import updatePlayerDict

def flatbet(betwon, playerDict):
    # This is just straight flat betting strategy, used as a control
    # The bet is the same each round, no matter the previous result
    if playerDict['bankroll'] > playerDict['bet']:
        if betwon:
            playerDict['bankroll'] += playerDict['bet']
            playerDict = updatePlayerDict(playerDict)
        else:
            playerDict['bankroll'] -= playerDict['bet']
            playerDict = updatePlayerDict(playerDict)
    return playerDict

# Bet sizing functon
def mg(betsize):
        betsize *= 2
        return betsize

def martingale(betwon, playerDict):
    # According to this strategy - players bet is doubled on a loss
    # On a win, the bet returns to the original unit size
    if playerDict['bankroll'] > playerDict['bet']:
        if betwon:
            playerDict['bankroll'] += playerDict['bet']
            playerDict['bet'] = playerDict['unit']
            playerDict = updatePlayerDict(playerDict)
        else:
            playerDict['bankroll'] -= playerDict['bet']
            playerDict['bet'] = mg(playerDict['bet'])
            playerDict = updatePlayerDict(playerDict)
    return playerDict

# Bet sizing function
def gmg(unitsize, betsize):
        betsize *= 2
        betsize += unitsize
        return betsize

def grandmartingale(betwon, playerDict):
    # According to this strategy - players bet is doubled, then one unit is added on every loss
    # On a win, the bet returns to the original unit size
    if playerDict['bankroll'] > playerDict['bet']:
        if betwon:
            playerDict['bankroll'] += playerDict['bet']
            playerDict['bet'] = playerDict['unit']
            playerDict = updatePlayerDict(playerDict)
        else:
            playerDict['bankroll'] -= playerDict['bet']
            playerDict['bet'] = gmg(playerDict['unit'], playerDict['bet'])
            playerDict = updatePlayerDict(playerDict)
    return playerDict

def labouchereWinCalc(playerDict, sequence):
    if len(playerDict['betprogression']) >2:
        # remove previous bet
        del playerDict['betprogression'][0]
        del playerDict['betprogression'][-1]
        # create next bet
        playerDict['bet'] = playerDict['betprogression'][0] + playerDict['betprogression'][-1]
    elif len(playerDict['betprogression']) == 2:
        # remove previous bet
        del playerDict['betprogression'][0]
        del playerDict['betprogression'][-1]
        # Add new sequence and restart
        playerDict.update({'betprogression':sequence[:]})
        # create next bet
        playerDict['bet'] = playerDict['betprogression'][0] + playerDict['betprogression'][-1]
    elif len(playerDict['betprogression']) == 1:
        del playerDict['betprogression'][0]
        # Add new sequence and restart
        playerDict.update({'betprogression':sequence[:]})
        # create next bet
        playerDict['bet'] = playerDict['betprogression'][0] + playerDict['betprogression'][-1]
    elif len(playerDict['betprogression']) == 0:
        # Add new sequence and restart
        playerDict.update({'betprogression':sequence[:]})
        # create next bet
        playerDict['bet'] = playerDict['betprogression'][0] + playerDict['betprogression'][-1]
    return playerDict

def labouchereLoseCalc(playerDict):
    # creates the next bet
    if len(playerDict['betprogression']) >2:
        playerDict['bet'] = playerDict['betprogression'][0] + playerDict['betprogression'][-1]
    elif len(playerDict['betprogression']) == 2:
        playerDict['bet'] = playerDict['betprogression'][0] + playerDict['betprogression'][-1]
    elif len(playerDict['betprogression']) == 1:
        playerDict['bet'] = playerDict['betprogression'][0] + playerDict['betprogression'][-1]
    elif len(playerDict['betprogression']) == 0:
        # should never be reached according to labouchere strategy
        print('ERROR labcouchereLoseCalc: betprogression == 0')
    return playerDict

def labouchere(betwon, playerDict, sequence):
    # Labouchere strategy dictates that on a win, the first and last element are removed
    # The next bet will then be the new 1st and last element summed
    # On a loss the losing bet is added to the end of the list
    # New bet is then created by summing the first and last element
    if playerDict['bankroll'] > playerDict['bet']:
        if betwon:
            playerDict['bankroll'] += playerDict['bet']
            playerDict = labouchereWinCalc(playerDict, sequence)
            playerDict = updatePlayerDict(playerDict)
        else:
            playerDict['bankroll'] -= playerDict['bet']
            #Bet lost, func doesn't update the dict
            playerDict['betprogression'].append(playerDict['bet']) # add last bet to the progression
            playerDict = labouchereLoseCalc(playerDict)
            playerDict = updatePlayerDict(playerDict)
    return playerDict

def parolicalc(playerDict):
    if playerDict['bethistory'][-1] == 4:
        playerDict['bet'] = playerDict['unit']
    elif playerDict['bethistory'][-1] < 4:
        playerDict['bet'] *= 2
    return playerDict

def paroli(betwon, playerDict):
    # Paroli dictates that the player doubles their bet after each win, up to 3 consecutive wins
    if playerDict['bankroll'] > playerDict['bet']:
        if betwon:
            playerDict['bankroll'] += playerDict['bet']
            playerDict = updatePlayerDict(playerDict)
            playerDict = parolicalc(playerDict)
        else:
            playerDict['bankroll'] -= playerDict['bet']
            playerDict = updatePlayerDict(playerDict)
            playerDict['bet'] = playerDict['unit']    
    return playerDict

'''
# Generic betting strategy function - copy for future strategies and modify as needed
def flatbet(betwon, playerDict):
    # This is just straight flat betting strategy, used as a control
    # The bet is the same each round, no matter the previous result
    if playerDict['bankroll'] > playerDict['bet']:
        playerDict['spinscompleted'] += 1
        if betwon:
            playerDict['bankroll'] += playerDict['bet']
            playerDict['history'].append(playerDict['bankroll'])
            playerDict['bethistory'].append(playerDict['bet'])
        else:
            playerDict['bankroll'] -= playerDict['bet']
            playerDict['history'].append(playerDict['bankroll'])
            playerDict['bethistory'].append(playerDict['bet'])
    return playerDict
'''