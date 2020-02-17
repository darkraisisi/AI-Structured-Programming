myList = [1,1,1,1,1,3,5,7,8,3,2,7,43,22,1,3,2,6,8]

def sortList(listToSort):
    for i in range(1, len(listToSort)): 
        key = listToSort[i] 
        j = i-1
        while j >= 0 and key < listToSort[j] : 
                listToSort[j + 1] = listToSort[j] 
                j -= 1
        listToSort[j + 1] = key
    
    return listToSort
    # return listToSort.sort()

print(sortList(myList))