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


#returned True als een rij geschikt is voor checkNumber
def rowCheck(rowIndex, checkNumber):
    row = sudoku[rowIndex]
    for i in range(8):
        number = int(row[i])
        if checkNumber == number:
            return True
    return False

#Returned True als een kolom geschikt is voor checkNumber
def collCheck(collIndex, checkNumber):
    for i in range(8):
        number = int(sudoku[i][collIndex])
        if number == checkNumber:
            return False
    return True
""""
def makeSq(hor, vert):
    tempSq = [[0 for p in range(3)]for q in range(3)]
    print (tempSq)
    for i in range(3):
        for j in range(3):
            tempSq[j][i] = sudoku[vert][hor]
            print (vert, "vert")
            print (hor, "hor")
            print (sudoku[vert][hor], "list")
            hor += 1
        vert += 1
"""

# Kijkt of een specifieke plek in de sudoku geschikt is voor een nummer
# Returned True als de plek geschikt is
def spotCheck(spotIndex, checkNumber):
    if rowCheck(spotIndex[0], checkNumber) or collCheck(spotIndex[1], checkNumber):
        return False
    return True

print(spotCheck([1,1], 4))
