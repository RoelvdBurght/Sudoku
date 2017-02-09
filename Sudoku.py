# dimensies array
w = 9
h = 9

#maakt array aan
sudoku = [[0 for x in range(w)] for y in range(h)]

#opent file en assignt de lijnen
sudokuFile = open("puzzle1.sudoku", "r")
horLijnDict = {}
x = 0
for line in sudokuFile:
    #print (line)
    line = line.replace(',', '')
    #print (line)
    horLijnDict[x] = line
    ++x

print (horLijnDict[0])


for x in range(len(sudoku)):
    for y in range(len(sudoku)):
        horLijnDict[]
        sudoku[x][y] = horLijnDict[]
