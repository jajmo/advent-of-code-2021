INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def getInput():
    with open(INPUT_FILE, 'r') as f:
        return f.read().splitlines()

def partOne():
    inp = getInput()
    prev = int(inp[0].strip())
    increasing = 0

    for line in inp:
        line = int(line.strip())
        if line > prev:
            increasing += 1
        prev = line

    return increasing

def partTwo():
    inp = getInput()
    increasing = firstSum = secondSum = place = 0
    total = len(inp)

    while place < total - 2:
        val = int(inp[place].strip()) + int(inp[place + 1].strip()) + int(inp[place + 2].strip())
        if firstSum == 0:
            firstSum = val
        else:
            secondSum = val

        if firstSum != 0 and secondSum != 0:
            if secondSum > firstSum:
                increasing += 1

            firstSum = secondSum
            secondSum = 0

        place += 1

    return increasing

if __name__ == "__main__":
    one = partOne()
    two = partTwo()
    print(f"Part one: {one}")
    print(f"Part two: {two}")