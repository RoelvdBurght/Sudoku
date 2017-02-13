# dimensies array
w = 9
h = 9

#opent file en assignt de lijnen in een dictionary
sudokuFile = open("puzzle1.sudoku", "r")
horLijnDict = {}
x = 0       #als iemand hier een elegantere oplossing voor heeft: graag
for line in sudokuFile:
    line = line.replace(',', '')    #haalt kommas eruit
    horLijnDict[x] = line
    x +=1


#maakt array aan
sudoku = [[0 for x in range(w)] for y in range(h)]
#knalt de lijnen in het array
for x in range(len(sudoku)):
    for y in range(len(sudoku)):
        str = horLijnDict[x]
        sudoku[x][y] = str[y]


#returnt True als checknumber voorkomt in gegeven rij
#row is een list
def rowCheck(row, checkNumber):
    for i in range(9):
        number = int(row[i])
        if checkNumber == number:
            return True

#returnt True als checknumber voorkomt in gegeven kolom
#coll is een int geen list zoals bij rowCheck
def collCheck(coll, checkNumber):
    for i in range(9):
        number = int(sudoku[i][coll])
        if number == checkNumber:
            return True

#maakt een 3x3 array van arrays uit de grote sudoku
#met hor & vert als linker bovenhoek
#returnt 3x3 blokje als output
def makeSq(hor, vert):
    tempSq = [[0 for p in range(3)]for q in range(3)]
    print (tempSq)
    for i in range(3):
        x = hor
        for j in range(3):
            tempSq[i][j] = sudoku[vert][x]
            x += 1
        vert += 1
    print(tempSq)
    return tempSq