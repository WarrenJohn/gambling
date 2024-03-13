from random import randint

rouletteTable = {
    0:"green",
    1:"red",
    2:"black",
    3:"red",
    4:"black",
    5:"red",
    6:"black",
    7:"red",
    8:"black",
    9:"red",
    10:"black",
    11:"black",
    12:"red",
    13:"black",
    14:"red",
    15:"black",
    16:"red",
    17:"black",
    18:"red",
    19:"red",
    20:"black",
    21:"red",
    22:"black",
    23:"red",
    24:"black",
    25:"red",
    26:"black",
    27:"red",
    28:"black",
    29:"black",
    30:"red",
    31:"black",
    32:"red",
    33:"black",
    34:"red",
    35:"black",
    36:"red"
}

def spinWheel():
    return randint(0,36)

def getColors(results):
    colors = []
    red = 0
    black = 0
    green = 0
    for a in results:
        colors.append(rouletteTable[a])
        if rouletteTable[a] == 'red':
            red += 1
        elif rouletteTable[a] == 'black':
            black += 1
        else:
            green += 1
    return colors, red, black, green

def getOddEven(results):
    oddEven = []
    odd = 0
    even = 0
    for a in results:
        if a != int(0):
            if a % 2:
                oddEven.append('odd')
                odd +=1
            else:
                oddEven.append('even')
                even +=1
    return oddEven, odd, even

# Add bet payouts, high and low numbers, max and min bet sizes, dozens and columns