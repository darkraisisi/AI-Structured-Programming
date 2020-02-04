def count(numberList:list,search:int):
    # print(numberList,search)
    amount = 0
    for number in numberList:
        if(number == search):
            amount +=1
    return amount

def maxDiff(numberList:list):
    largestDiff = 0
    i = 0
    for number in numberList:
        if(i == len(numberList)-1):
            return largestDiff
        diff = numberList[i] - numberList[i+1]
        if(diff > largestDiff):
            largestDiff = diff
        i +=1

def binListValidate(binList:list):
    # returns true als er meer eenen dan nullen zijn
    # returns false als dit niet zo is
    # returns -1 als er meer dan 12 zijn
    limit = 12
    ones = 0
    for num in binList:
        if(num == 0):
            if(limit == 0):
                return -1
            else:
                limit -=1
        else:
            ones +=1
    # print(f'length: {len(binList)}, 1\'s: {ones}, sub: {len(binList) - ones}, stmnt: {len(binList) - ones > ones}')
    if(len(binList) - ones > ones):
        return False
    else:
        return True
# Lijst voor vergelijkingen
myList = [1,1,1,1,1,3,5,7,8,3,2,7,43,22,1,3,2,6,8]
# deze lijst heeft meer dan 12 nullen
binListMax = [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0]
binListLess = [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0]
binListMore = [1,1,1,1,0,0,0,0,0,1,1,1,1,0]

print(count(myList,1))
print(maxDiff(myList))

print(binListValidate(binListMax))
print(binListValidate(binListLess))
print(binListValidate(binListMore))
