import colors as col

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