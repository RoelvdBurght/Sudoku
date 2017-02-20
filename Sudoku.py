# dimensies array
w = 9
h = 9

# opent file en assignt de lijnen in een dictionary
sudokuFile = open("puzzle1.sudoku", "r")
horLijnDict = {}
x = 0       #als iemand hier een elegantere oplossing voor heeft: graag
for line in sudokuFile:
    line = line.replace(',', '')    #haalt kommas eruit
    horLijnDict[x] = line
    x +=1


#maakt array aan
sudoku = [[0 for x in range(w)] for y in range(h)]
# knalt de lijnen in het array
for x in range(len(sudoku)):
    for y in range(len(sudoku)):
        str = horLijnDict[x]
        sudoku[x][y] = int(str[y])


#returned True als een rij geschikt is voor het nummer checkNumber
def rowCheck(rowIndex, checkNumber):
    row = sudoku[rowIndex]
    for i in range(9):
        number = row[i]
        if checkNumber == number:
            return False
    return True

#Returned True als een kolom geschikt is voor checkNumber
def collCheck(collIndex, checkNumber):
    for i in range(9):
        print(i)
        number = int(sudoku[i][collIndex])
        if number == checkNumber:
            return False
    return True

#maakt een 3x3 array van arrays uit de grote sudoku
#met hor & vert als linker bovenhoek
#returnt 3x3 blokje als output
def makeSq(array):
    hor = array[0]
    vert = array[1]
    tempSq = [[0 for p in range(3)]for q in range(3)]
    for i in range(3):
        x = hor
        for j in range(3):
            tempSq[i][j] = sudoku[vert][x]
            x += 1
        vert += 1
    return (tempSq)

def getCornerCoordinates(x, y):
    correctionX = x%3
    correctionY = y%3
    return [x-correctionX, y-correctionY]

def sqCheck(x, y, checkNumber):
    coordinates = getCornerCoordinates(x, y)
    tempSq = makeSq(coordinates)
    for i in range(3):
        for j in range(3):
            number = tempSq[i][j]
            if (number == checkNumber):
                return False
    return True

# Kijkt of een specifieke plek in de sudoku geschikt is voor een nummer
# Returned True als de plek geschikt is
def spotCheck(spotIndex, checkNumber):
    if rowCheck(spotIndex[0], checkNumber) or collCheck(spotIndex[1], checkNumber):
        return False
    return True

def usableInts( row ):
    usable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    existingrow = sudoku[row]
    for i in range(len(existingrow)):
        if existingrow[i] != 0:
            usable.remove(existingrow[i])






