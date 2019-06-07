effective=[]

def putQueen(x, y, x_, y_):
    # sameRow or sameCol or diagonallyLeft or diagonallyRight 
    return not (x==x_ or y==y_ or x-x_==y-y_ or x-x_==y_-y)

def printBord(effective):
    for i in effective:
        row = ['□' for _ in range(8)]
        row[i] = 'Q'
        print(''.join(row))
    print('\n', '-'*20, '\n')

def eightQueen(i):
    # row range
    if i < 8:
        # col range
        for j in range(8):
            if all([putQueen(i, j, x, effective[x]) for x in range(i)]) :
                effective.append(j)
                # next row
                eightQueen(i+1)
                effective.pop()
    else:
        printBord(effective)

eightQueen(0)