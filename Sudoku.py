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

#maakt een 3x3 array van arrays uit de grote sudoku
#met hor & vert als linker bovenhoek
#returnt 3x3 blokje als output

def makeSq(vert, hor):
    tempSq = [[0 for p in range(3)]for q in range(3)]
    print (tempSq)
    for i in range(3):
        x = hor
        for j in range(3):
            tempSq[i][j] = sudoku[vert][x]
            x += 1
        vert += 1
    return (tempSq)


# Kijkt of een specifieke plek in de sudoku geschikt is voor een nummer
# Returned True als de plek geschikt is
def spotCheck(spotIndex, checkNumber):
    if rowCheck(spotIndex[0], checkNumber) or collCheck(spotIndex[1], checkNumber):
        return False
    return True


x = makeSq(3,3)
print(x)
def checkSq(array[][]):
    spotCounter = -1
    for i in range(2):
        for j in range(2):
            spotCounter += 1
            if array[i][j] == 0:
                