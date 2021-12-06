INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()

    bingoNumbers = map(int, lines[0].split(','))
    bingoBoards = []
    matchedNumbers = []
    currentBoard = -1

    for line in lines[1:]:
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
        if bingo != None:
            break
    print(getScore(bingoBoards[bingo], matchedNumbers[bingo], calledNumber))

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
    # First, check across
    for boardIdx, board in enumerate(matchedNumbers):
        for rowIdx, row in enumerate(board):
            if row == [1] * len(row):
                return boardIdx

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
                return bingo

            row = 0
            col += 1

    return None

def getScore(board, matchedNumbers, calledNumber):
    unmarkedSum = 0;
    for rowIdx, row in enumerate(board):
        for colIdx, col in enumerate(board):
            if matchedNumbers[rowIdx][colIdx] == 0:
                unmarkedSum += board[rowIdx][colIdx]

    return unmarkedSum * calledNumber

if __name__ == "__main__":
    main()