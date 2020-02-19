import colors as col
import random

def evaluateColors(guessedColors: list,secretCode) -> dict:
    tempColors = secretCode[:]
    tempGuessedColors = guessedColors[:]
    pins = {
        'black': 0,
        'white': 0
    }
    j = 0
    for i in range(0, len(secretCode)):
        j +=1
        if secretCode[i] == guessedColors[i]:
            pins['black'] += 1
            j -=1
            del tempColors[j]
            del tempGuessedColors[j]

    for guessedColor in tempGuessedColors:
        try:
            i = tempColors.index(guessedColor)
            if tempColors[i] == guessedColor:
                pins['white'] +=1
                del tempColors[i]
        except ValueError:
            pass
    return pins

def generateAllCombinations():
    arr = []
    for colorOne in col.all_colors:
        for colorTwo in col.all_colors:
            for colorThree in col.all_colors:
                for colorFour in col.all_colors:
                    arr.append([colorOne,colorTwo,colorThree,colorFour])
    print('populate for all')
    return arr

allPossibleCombinations = generateAllCombinations()
mutableAllPossibleCombinations = []

def repopulateAllCombinations():
    global allPossibleCombinations
    global mutableAllPossibleCombinations
    mutableAllPossibleCombinations = [*allPossibleCombinations]

repopulateAllCombinations()

def generateSecret(amount=4):
    col.SECRET = []
    for i in range(0,amount):
        col.SECRET.append(col.all_colors[random.randint(0,len(col.all_colors)-1)])

def simpleAlgorithm(turn,secret):
    global mutableAllPossibleCombinations
    if(turn == 0):
        currentGuesse = ['Red', 'Red', 'Green', 'Blue']
    else:
        # currentGuesse = getFirstPosibility()
        currentGuesse = getMiddlePosibility()

    masterPins = evaluateColors(currentGuesse,secret)
    i = 0
    tmp = mutableAllPossibleCombinations[:]
    for possibility in mutableAllPossibleCombinations:
        pins = evaluateColors(currentGuesse,possibility)

        if(masterPins != pins):
            tmp.remove(possibility)

    mutableAllPossibleCombinations = tmp
    return masterPins

def getFirstPosibility():
    return mutableAllPossibleCombinations.pop(0)

def getMiddlePosibility():
    item = mutableAllPossibleCombinations[int(len(mutableAllPossibleCombinations) /2)]
    mutableAllPossibleCombinations.remove(item)
    return item