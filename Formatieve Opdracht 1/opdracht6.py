myList = [1,1,1,1,1,3,5,7,8,3,2,7,43,22,1,3,2,6,8]
my2DList = [
    [1,1,1,1,1,3,5,7,8,3,2,7,43,22,1,3,2,6,8],
    [1,1,1,1,1,3,5,7,8,3,2,7,43,22,1,3,2,6,8],
    [1,1,1,1,1,3,5,7,8,3,2,7,43,22,1,3,2,6,8],
    [1,1,1,1,1,3,5,7,8,3,2,7,43,22,1,3,2,6,8],
    [1,1,1,1,1,3,5,7,8,3,2,7,43,22,1,3,2,6,8],
    [1,1,1,1,1,3,5,7,8,3,2,7,43,22,1,3,2,6,8]
]
def averageFromList(_list:list):
    return sum(_list) / len(_list)

def averageFrom2DList(_2Dlist):
    total = [(sum(_list) / len(_list)) for _list in _2Dlist]
    return sum(total) / len(total)

print(averageFromList(myList))
print(averageFrom2DList(my2DList))