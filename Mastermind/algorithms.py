import colors as col
import random
# Source for algorithms: Kooi B. 'Yet another mastermind strategy', https://www.rug.nl/research/portal/files/9871441/icgamaster.pdf used on and before 19-02-2020

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

def repopulateAllCombinations():
    global allPossibleCombinations
    global mutableAllPossibleCombinations
    mutableAllPossibleCombinations = [*allPossibleCombinations]

allPossibleCombinations = generateAllCombinations()
mutableAllPossibleCombinations = []

repopulateAllCombinations()

def generateSecret(amount=4):
    col.SECRET = []
    for i in range(0,amount):
        col.SECRET.append(col.all_colors[random.randint(0,len(col.all_colors)-1)])

"""
This algorithm is made as described in 'Yet another mastermind strategy'.
It also function as described, with expected results around 4.6 tries on average.
"""
def simpleAlgorithm(turn,secret):
    if(turn == 0):
        currentGuesse = ['Red', 'Red', 'Green', 'Blue']
    else:
        # currentGuesse = gePosibilityFromIndex(0)
        currentGuesse = gePosibilityFromIndex(int(len(mutableAllPossibleCombinations) /2))

    masterPins = evaluateColors(currentGuesse,secret)
    filterPosibilityList(currentGuesse,masterPins)
    return masterPins

"""
This heuristic algorithm is made by me in a small effort to try and improve on the simple algorithm as described in 'Yet another mastermind strategy'.
The strategy was to broaden the removed amount of items by chosing a guess from oppositeparts of the list each time.

My changes have however little to no effect.
"""
def heuristicAlgorithm(turn,secret):
    if(turn == 0):
        currentGuess = ['Red', 'Green', 'Blue', 'Yellow']
    elif turn % 2 == 0:
        currentGuess = gePosibilityFromIndex(int(len(mutableAllPossibleCombinations) /4))
    else:
        currentGuess = gePosibilityFromIndex(int((len(mutableAllPossibleCombinations) /4)*3))

    masterPins = evaluateColors(currentGuess,secret)
    filterPosibilityList(currentGuess,masterPins)

    return masterPins

def gePosibilityFromIndex(index):
    item = mutableAllPossibleCombinations[index]
    mutableAllPossibleCombinations.remove(item)
    return item

def filterPosibilityList(currentGuesse,masterPins):
    global mutableAllPossibleCombinations
    tmp = mutableAllPossibleCombinations[:]

    for possibility in mutableAllPossibleCombinations:
            pins = evaluateColors(currentGuesse,possibility)

            if(masterPins != pins):
                tmp.remove(possibility)

    mutableAllPossibleCombinations = tmp
"""
This funciton gathers all the combinations and assignes the amount that combinations has hit to each option in the list.
This is done so we can asses the best guess in every worstcase situation.
As you can imagne this will take a rather long time and is not much better than the simple sort.
"""
def partitionSize():
    # This function makes me want to cry
    partitions = {}
    for possibility in mutableAllPossibleCombinations:
        key = ','.join(possibility) # the key is the combination it self.
        partitions[key] = {'4,0': 0, '3,0': 0, '2,0': 0, '1,0': 0, '2,2': 0, '1,2': 0, '0,2': 0, '2,1': 0, '1,1': 0, '0,1': 0, '0,0': 0, '1,3': 0, '0,3': 0, '0,4': 0} # with value all the hits on combinations

        for _possibility in mutableAllPossibleCombinations:
            # Compare all the combinations to one another and update the partitions dict with the hits.
            _pins = evaluateColors(possibility,_possibility)
            pinToStr = f"{_pins['black']},{_pins['white']}"
            partitions[key][pinToStr] +=1
    
    highestPerPartition = {}

    for partitionKey in partitions:
        # Get the most likely scenario per possibility.
        highestKey = max(partitions[partitionKey], key=partitions[partitionKey].get)
        # Add all the posibilities to a dict with the key as the combination, the amount from the most likely outcome is its value.
        highestPerPartition[partitionKey] = partitions[partitionKey][highestKey]

    # From all the worst case scenario's get the best one.
    best = min(highestPerPartition, key=highestPerPartition.get)

    return best.split(',') # Make the guesse by decoding the key

"""
This algorithm uses the partition sizing that is mentiond in 'Yet another mastermind strategy'.
For game state i calculate all the possible worstcase scenario's and get the best one for my next guess
"""
def consistentWorstCaseAlgorithm(turn:int,secret):
    global mutableAllPossibleCombinations
    if(turn == 0):
        currentGuesse = ['Red', 'Red', 'Green', 'Green']
    else:
        currentGuesse = partitionSize()

    masterPins = evaluateColors(currentGuesse,secret)
    filterPosibilityList(currentGuesse,masterPins)
    
    return masterPins