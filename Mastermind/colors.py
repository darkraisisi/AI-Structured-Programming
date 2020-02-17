all_colors = ['Red', 'Yellow', 'Blue', 'Green', 'Orange', 'Purple']
SECRET = ['Red', 'Green', 'Blue', 'Yellow']
# ['Green','Green','Red','Yellow']

# def evaluateColors(guessedColors: list) -> dict[int,int]:
def evaluateColors(guessedColors: list,secretCode) -> dict:


    tempColors = secretCode[:]
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

    for guessedColor in guessedColors:
        try:
            i = tempColors.index(guessedColor)
            if tempColors[i] == guessedColor:
                pins['white'] +=1
                del tempColors[i]
        except ValueError:
            pass
    return pins