def fibonaci(_max,_list=[0,1]):
    if(len(_list) == _max):
        return _list
    _list.append(_list[-1]+_list[-2])
    return fibonaci(_max,_list)

print(fibonaci(20))