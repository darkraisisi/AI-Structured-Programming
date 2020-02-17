def fibonaci_1(_max,_list=[0,1]):
    if(len(_list) == _max):
        return _list
    _list.append(_list[-1]+_list[-2])
    return fibonaci_1(_max,_list)

first = 0
second = 1

def fibonaci_2(n):
    global first
    global second
    print(n)
    n -=1
    if n == 0:
        return total
    total = first + second
    first = second
    second = total
    
    return total + fibonaci_2(n)

print(fibonaci_1(20))
print(fibonaci_2(20))
