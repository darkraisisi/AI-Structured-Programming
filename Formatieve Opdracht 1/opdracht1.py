def drawPyramideFor(height: int):
    i = 1
    for i in range(height):
        print(i*'*')
    for i in range(height):
        print((height-i)*'*')


def drawPyramideWhile(height: int):
    i = 1
    while i != height+1:
        print(i*'*')
        i += 1
        pass
    i = 1
    while i != height:
        print((height-i)*'*')
        i += 1
        pass

def drawPyramideForRightSide(height: int):
    i = 1
    for i in range(height):
        print(('{:>{}}').format(i*'*',height))
    for i in range(height):
        print(('{:>{}}').format((height-i)*'*',height))

drawPyramideFor(int(input('Pyramide met ForLoop\nCijfer hier: ')))

drawPyramideWhile(int(input('Pyramide met WhileLoop\nCijfer hier: ')))
drawPyramideForRightSide(int(input('Pyramide met WhileLoop Align Right\nCijfer hier: ')))