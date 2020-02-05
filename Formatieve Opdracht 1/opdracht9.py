# Python 3.2+ is nodig
def charShift(char,n):
    _bin = format(ord(char), 'b')
    _bin = '1234567'
    if(n>0):
        # rotate left
        front = _bin[0:n]
        back = _bin[n:len(_bin)]
        return back+front
        # return _bin[n:len(_bin)] + _bin[0:n]
    else:
        # rotate right
        n = abs(n)
        i = 0
        _bin = list(_bin)
        for num in _bin:
            if i < n:
                if(n+i >= len(_bin)):
                    rollover = ((n+i)-len(_bin))
                    test = _bin.pop(i)
                    ret = _bin[rollover]
                    _bin.insert(0,test)
                    i = i+1
                else:
                    ret = _bin[n+i]
                    _bin[n+i] = num
                    _bin[i] = ret
                    i = i+1
        return ''.join(_bin)

print(charShift('a',4))
print(charShift('a',-4))
