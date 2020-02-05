def stringToCeasarCypher(text,rot):
    newTextList = []
    for letter in text:
        if(letter != ' '):
            char = ord(letter)
            # print(f"Letter: {letter}, char: {char}")
            if(char+rot < 122):#checken of er rollover is zo ja dan het verschil aftrekken
                newTextList.append(chr(char + rot))
            else:
                newTextList.append(chr(char + rot - 57))
        else:
            newTextList.append(' ')
    return ''.join(newTextList)

print(stringToCeasarCypher(input("Please input a text for the rotation\n"),int(input("Please input an amount for rotation: "))))
# print(stringToCeasarCypher('abc xyz',3))