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
        number = (sudoku[i][collIndex])
        if number == checkNumber:
            return False
    return True

#maakt een 3x3 array van arrays uit de grote sudoku
#met hor & vert als linker bovenhoek
#returnt 3x3 blokje als output
def makeSq(col, row):
    tempSq = [[0 for p in range(3)]for q in range(3)]
    for i in range(3):
        x = col
        for j in range(3):
            tempSq[i][j] = sudoku[row][x]
            x += 1
        row += 1
    return (tempSq)

def getCornerCoordinates(x):
    correctionX = x%3
    return x-correctionX

# Neemt de coördinaten van een plek en een nummer als input.
# Returned true als de plek geschikt is, en anders False
def sqCheck(row, col, checkNumber):
    tempSq = makeSq(getCornerCoordinates(col), getCornerCoordinates(row))
    for i in range(3):
        for j in range(3):
            number = tempSq[i][j]
            if (number == checkNumber):
                return False
    return True

# Kijkt of een specifieke plek in de sudoku geschikt is voor een nummer
# Returned True als de plek geschikt is
def spotCheck(row, col, checkNumber):
    if sqCheck(row, col, checkNumber) == True and collCheck(col, checkNumber) == True:
        return True
    return False


# Returns a list with usable ints for the input row
def usableInts(row):
    usable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    existingrow = sudoku[row]
    #existingrow = list(map(int, existingrow))
    for i in range(len(existingrow)):
        if existingrow[i] != 0:
            usable.remove(existingrow[i])
    return usable

#print(usableInts(0))
# Returned False als er een nul in de sudoku zit
def isSudokuFilled(sudoku):
    for i in range(h):
        for j in range(w):
            if sudoku[i][j] == 0:
                return False
    return True


def solveRow(row):
    tempList = usableInts(row)
    for num in tempList:
        possible = possibleInRow(row, num)
        if possible == 1:
            placeNumber(row, num)
            tempList.remove(num)

def possibleInRow(row, num):
    counter = 0
    for j in range(9):
        if spotCheck(row, j, num) == True and sudoku[row][j] == 0:
            counter += 1
    return counter


def placeNumber(row, num):
    for j in range(9):
        if spotCheck(row, j, num) == True:
            if sudoku[row][j] == 0 and spotCheck(row, j, num) == True:
                sudoku[row][j] = num

def solveSudoku(sudoku):
    while isSudokuFilled(sudoku) == False:
        for i in range(9):
            solveRow(i)

'''solveRow(0)
solveRow(1)
solveRow(2)
solveRow(3)
solveRow(4)
solveRow(5)
solveRow(6)
solveRow(7)
solveRow(8)
'''
solveSudoku(sudoku)
print(sudoku)
""""
def knalleuh(sudoku):
    for i in range(row):
        tempList = usableInts(row)
        for j in range(col):
            if sudoku[row][col] == 0
                counter = 0
                for len(tempList):
                    if(collCheck(col, tempList[counter]) == True && sqCheck(row, col, tempList[counter]) == True)
                    als beide bovenstaande evaluaties true zijn
                        onthoud plek en getal dat daar kan
                als er 2 getallen kunnen -> volgend hokje
                als er 1 getal kan -> vul dat getal in
    check of sudoku gevuld is
"""