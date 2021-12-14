INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def getInput():
    maxX = maxY = 0
    with open(INPUT_FILE, 'r') as f:
        inp = f.read().splitlines()

    folds = []
    matrix = []
    inFolds = False

    for x in inp:
        if x == '':
            break

        split = list(map(int, x.split(',')))
        maxX = maxX if maxX > split[0] else split[0]
        maxY = maxY if maxY > split[1] else split[1]

    maxX += 1
    maxY += 1

    for i in range(maxY):
        matrix.append([])
        matrix[i] = ['.'] * maxX

    for x in inp:
        if x == '':
            inFolds = True
            continue

        if inFolds:
            folds.append(x.split('fold along ')[1].split('='))
        else:
            split = list(map(int, x.split(',')))
            matrix[split[1]][split[0]] = '#'

    return [matrix, folds]

def partOne():
    matrix, folds = getInput()
    matrix = doFold(*folds[0], matrix)
    visible = 0
    for i in matrix:
        visible += i.count('#')

    return visible

def doFold(direction, num, matrix):
    num = int(num)
    if direction == 'x':
        newMatrix = []
        for i, j in enumerate(matrix):
            newMatrix.append([])
            newMatrix[i] = matrix[i][:num]
    else:
        newMatrix = matrix[:num]

    for idx, i in enumerate(matrix):
        if direction == 'y' and idx < num:
                continue
        for idx2, j in enumerate(i):
            if direction == 'x' and idx2 < num:
                continue
            x = idx2 if direction == 'y' else num - (idx2 - num)
            y = idx if direction == 'x' else num - (idx - num)
            if j == '#':
                newMatrix[y][x] = '#'

    return newMatrix

def partTwo():
    matrix, folds = getInput()

    for fold in folds:
        matrix = doFold(*fold, matrix)

    pp(matrix)

    return 0

def pp(j):
    for i in j:
        print(''.join(i))

if __name__ == "__main__":
    one = partOne()
    two = partTwo()
    print(f"Part one: {one}")
    print(f"Part two: {two}")