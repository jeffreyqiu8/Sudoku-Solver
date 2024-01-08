#Sudoku Solver
def findSquare(row, col):
    return (row-(row%3), col-(col%3))
def solve(sud):
    count = 0
    reps = 0
    for row in sud:
        for col in row:
            if col == '*':
                count +=1
    while count>0:
        check=count
        for row in range(len(sud)):
            for col in range(len(sud[row])):
                if sud[row][col] == '*':
                    #find possibilities
                    poss = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    for x in range(len(sud)):
                        if sud[x][col] in poss:
                            poss.remove(sud[x][col])
                    for x in range(len(sud[row])):
                        if sud[row][x] in poss:
                            poss.remove(sud[row][x])
                    square = findSquare(row, col)
                    for x in range(square[0], square[0]+3):
                        for y in range(square[1], square[1]+3):
                            if sud[x][y] in poss:
                                poss.remove(sud[x][y])
                                
                    if len(poss) == 1:
                        sud[row][col] = poss[0]
                        count-=1
                    else:
                        sud[row][col] = poss
                elif isinstance(sud[row][col], list):
                    # update possibilities
                    poss = sud[row][col]
                    for x in range(len(sud)):
                        if sud[x][col] in poss:
                            poss.remove(sud[x][col])
                    for x in range(len(sud[row])):
                        if sud[row][x] in poss:
                            poss.remove(sud[row][x])
                    square = findSquare(row, col)
                    for x in range(square[0], square[0]+3):
                        for y in range(square[1], square[1]+3):
                            if sud[x][y] in poss:
                                poss.remove(sud[x][y])
                                
                    if len(poss) == 1:
                        sud[row][col] = poss[0]
                        count-=1
                    else:
                        sud[row][col] = poss
    #checks every possibility for each blank square to see if the number must be in that square
    
        for row in range(len(sud)):
            for col in range(len(sud[row])):
                if isinstance(sud[row][col], list):
                    for x in sud[row][col]:
                        #check row
                        onlyposs = True
                        for y in range(len(sud)):
                            if isinstance(sud[y][col], list) and x in sud[y][col] and y != row:
                                onlyposs = False
                            elif isinstance(sud[y][col], int) and x==sud[y][col]:
                                onlyposs = False
                        if onlyposs:
                            sud[row][col] = x
                            count-=1
                        #check col
                        onlyposs = True
                        for y in range(len(sud[row])):
                            if isinstance(sud[row][y], list) and x in sud[row][y] and y != col:
                                onlyposs = False
                            elif isinstance(sud[row][y], int) and x==sud[row][y]:
                                onlyposs = False
                        if onlyposs:
                            sud[row][col] = x
                            count-=1
                        #check square
                        onlyposs = True
                        square = findSquare(row, col)
                        for y in range(square[0], square[0]+3):
                            for z in range(square[1], square[1]+3):
                                if isinstance(sud[y][z], list) and x in sud[y][z] and (y != row or z!=col):
                                    onlyposs = False
                                elif isinstance(sud[y][z], int) and x==sud[y][z]:
                                    onlyposs = False
                        if onlyposs:
                            sud[row][col] = x
                            count-=1
        if count == check:
            reps += 1
        else:
            reps =0
        #if reps ==3:
        #    break
    return sud
                
def printgrid(arr):
    for row in arr:
        for col in row:
            print(col, end="")
        print()
def main():
    sudoku = [['*','*','*',4,'*',9,'*','*','*'],
              ['*','*','*','*',6,'*','*','*','*'],
              [2,'*','*',5,'*','*','*',4,'*'],
              [5,'*',8,'*','*',3,'*','*',4],
              [3,'*','*',6,'*',7,'*','*',9],
              ['*','*',7,'*','*','*','*',3,6],
              [9,'*',6,'*',4,'*','*',1,'*'],
              ['*','*','*',7,'*','*','*','*','*'],
              ['*','*',3,8,'*','*',5,'*','*']]
    printgrid(sudoku)
    solve(sudoku)
    print()
    printgrid(sudoku)


if __name__ == "__main__":
    main()