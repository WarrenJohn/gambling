from roulette import rouletteTable

def oddOrEven(wheelResult):
    if wheelResult != int(0):
        if wheelResult % 2:
            result = 'odd'
        else:
            result = 'even'
    else:
        result = False
    return result

def betwon(playerbet, result):
    #only working for these bets: even, odd, red, black, green (0)
    if playerbet == rouletteTable[result]:
        #checks the dict for red, black, or green
        return True
    elif oddOrEven(result) == playerbet:
        #checks for an odd or even number
        return True
    else:
        return False
