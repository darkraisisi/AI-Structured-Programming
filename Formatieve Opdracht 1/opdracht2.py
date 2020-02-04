def stringDiff():
    strOne = input('Geef een string voor vergelijking: ')
    strTwo = input('Geef een string voor vergelijking: ')
    if(strOne == strTwo):
        return -1
    else:
        i = 0
        for i in range(len(min(strOne,strTwo))):
            if strOne[i] != strTwo[i]:
                return i
        return i+1
    
    
print(f'De index waar het verschil is: {stringDiff()}')