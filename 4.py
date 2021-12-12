INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def processCalledNumber(number, boards, matchedNumbers):
    for boardIdx, board in enumerate(boards):
        for rowIdx, row in enumerate(board):
            try:
                idx = row.index(number)
                matchedNumbers[boardIdx][rowIdx][idx] = 1
            except:
                continue
    return matchedNumbers

def checkForBingo(boards, matchedNumbers):
    winners = []
    # First, check across
    for boardIdx, board in enumerate(matchedNumbers):
        for rowIdx, row in enumerate(board):
            if row == [1] * len(row):
                winners.append(boardIdx)
                break

    # Second, check vertically
    for boardIdx, board in enumerate(matchedNumbers):
        row = col = 0
        rowSize = len(board)
        colSize = len(board[0])

        while col < colSize:
            bingo = True
            while row < rowSize and bingo == True:
                bingo = bingo and (board[row][col] == 1)
                row += 1

            if bingo:
                winners.append(boardIdx)
                break

            row = 0
            col += 1

    return winners

def getScore(board, matchedNumbers, calledNumber):
    unmarkedSum = 0;
    for rowIdx, row in enumerate(board):
        for colIdx, col in enumerate(board):
            if matchedNumbers[rowIdx][colIdx] == 0:
                unmarkedSum += board[rowIdx][colIdx]

    return unmarkedSum * calledNumber

def getInput():
    with open(INPUT_FILE, 'r') as f:
        return f.read().splitlines()

def partOne():
    inp = getInput()
    bingoNumbers = map(int, inp[0].split(','))
    bingoBoards = []
    matchedNumbers = []
    currentBoard = -1

    for line in inp[1:]:
        if line == "":
            currentBoard += 1
            bingoBoards.append([])
            matchedNumbers.append([])
            continue

        row = list(map(int, [i for i in line.split(' ') if i]))
        bingoBoards[currentBoard].append(row)
        matchedNumbers[currentBoard].append([0] * len(row))
    
    for calledNumber in bingoNumbers:
        matchedNumbers = processCalledNumber(calledNumber, bingoBoards, matchedNumbers)
        bingo = checkForBingo(bingoBoards, matchedNumbers)
        if len(bingo) > 0:
            break
    return getScore(bingoBoards[bingo[0]], matchedNumbers[bingo[0]], calledNumber)

def partTwo():
    inp = getInput()
    bingoNumbers = map(int, inp[0].split(','))
    bingoBoards = []
    matchedNumbers = []
    currentBoard = -1

    for line in inp[1:]:
        if line == "":
            currentBoard += 1
            bingoBoards.append([])
            matchedNumbers.append([])
            continue

        row = list(map(int, [i for i in line.split(' ') if i]))
        bingoBoards[currentBoard].append(row)
        matchedNumbers[currentBoard].append([0] * len(row))

    for calledNumber in bingoNumbers:
        matchedNumbers = processCalledNumber(calledNumber, bingoBoards, matchedNumbers)
        bingo = checkForBingo(bingoBoards, matchedNumbers)
        if len(bingo) > 0:
            if len(bingoBoards) > 1:
                bingoBoards = [v for i, v in enumerate(bingoBoards) if i not in bingo]
                matchedNumbers = [v for i, v in enumerate(matchedNumbers) if i not in bingo]
            elif len(bingoBoards) == 1:
                break

    return getScore(bingoBoards[bingo[0]], matchedNumbers[bingo[0]], calledNumber)

if __name__ == "__main__":
    one = partOne()
    two = partTwo()
    print(f"Part one: {one}")
    print(f"Part two: {two}")