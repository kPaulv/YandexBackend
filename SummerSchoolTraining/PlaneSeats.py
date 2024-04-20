# functions definition

# function for determining search start and search direction
def determineSearchStartAndDirection(request):
    # number of passengers
    num = int(request[0])
    # colRange is A-C() or D-F
    # colDirection is asc or desc
    colDirection = 'asc' # left + window
    # colStart is from window(0 or 6) or from aisle(2 or 4)
    colStart = 0 # left + window
    # determine start searching pos and search direction
    if(request[1] == 'left'):
        if(request[2] == 'aisle'):
            colStart = 2
            colDirection = 'desc'
    else:   # side = right
        colStart = 4 # right + aisle
        if(request[2] == 'window'):
            colStart = 6
            colDirection = 'desc'

    return num, colStart, colDirection


# function for determining start index and search direction
def determineSearchStep(colStart, colDirection, peopleAmount):
    # default search increment and search end
    step = 1
    end = colStart + peopleAmount
    # if descending search change the increment and end
    if(colDirection == 'desc'):
        step = -1
        end = colStart - peopleAmount
    
    return step, end


# function for iterationg through seats
def searchSeats(seatsMatrix, rows, colStart, colEnd, step, requestedSeatsAmount):
    result = True
    # seats available for group e.g. 1B, 1C
    groupSeats = []
    # free seats amount
    freeSeats = 0
    # iterating through matrix
    for row in range(rows):
        if freeSeats == requestedSeatsAmount:
            break
        freeSeats = 0
        result = True
        # 1B, 1C
        groupSeats = []
        # markedSeatsIndices
        markedSeats = []
        for col in range(colStart, colEnd, step):
            if seatsMatrix[row][col] == '#':
                result = False
                break
            else:
                # seats to mark 'X' and '#' later
                markedSeats.append([row, col])
                freeSeats += 1
                seatLetterCode = 65 + col
                if(col > 3):
                    seatLetterCode -= 1
                groupSeats.append(str(row + 1) + chr(seatLetterCode))
    
    return result, groupSeats, markedSeats


# rows amount (n)
rows = int(input())

# total cols = seats per row amount  + aisle = 6 + 1 = 7
cols = 7

# seatsMatrix
seatsMatrix = []

# input matrix
for i in range(rows):
    a = []
    for symbol in input():
         a.append(symbol)
    seatsMatrix.append(a)

# number of groups
m = int(input())

# iterate through all groups
for i in range(m):
    # request list e.g. [2, 'left', 'aisle']
    group = list(input().split())

    # number of passengers, search start index and search direction
    num, colStart, colDirection = determineSearchStartAndDirection(group)

    # default search increment and search end
    step, end = determineSearchStep(colStart, colDirection, num)

    # bool (can we fulfill request or not)
    canFulfill, groupSeats, markedSeats = searchSeats(seatsMatrix, rows, colStart, end, step, num)

    # if we can fulfill request mark the seats and print their numbers e.g. 1D 1E
    if canFulfill:
        groupSeats.sort()
        print('Passengers can take seats:', *groupSeats)
        # mark seats with 'X' for output
        for seat in markedSeats:
            seatsMatrix[seat[0]][seat[1]] = 'X'
        # print seats with 'X's
        for line in seatsMatrix:
            print(*line, sep='')
        # mark fulfilled request seats with '#'
        for seat in markedSeats:
            seatsMatrix[seat[0]][seat[1]] = '#'
    else:
        print('Cannot fulfill passengers requirements')
