def rotateString(text):
    if(len(text) == 1):
        return text
    newString = text[-1:]
    return newString + rotateString(text[:-1])

def palindrome(text):
    if(text.lower() == rotateString(text.lower())):
        return True
    else:
        return False

def rotateStringComp(text):
    return text[::-1]

print(palindrome('Testing'))
print(palindrome('legovogel'))

# Een libary die een woord omdraait?
# Ik had gezocht maar niks gevonden.