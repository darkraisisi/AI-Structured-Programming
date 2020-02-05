for i in range(1,101):
    ret = i
    if(i % 3 == 0):
        ret = 'fizz'
    if(i % 5 == 0):
        ret = 'buzz'
    if(i % 3 == 0 and i % 5 == 0):
        ret = 'fizzbuzz'
    print(ret)