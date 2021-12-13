INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"
octopi = []
flashes = []

def getInput():
    with open(INPUT_FILE, 'r') as f:
        return f.read().splitlines()

def partOne(partTwo):
    global octopi, flashes

    inp = getInput()
    flashed = 0
    rounds = 100

    octopi = [[-1] * (len(inp[0]) + 2)]
    for line in inp:
        octopi.append([-1] + list(map(int, list(line))) + [-1])
    octopi.append([-1] * (len(inp[0]) + 2))

    totalOctopi = len(inp) * len(inp[0])
    i = 1

    while True:
        # First increase each by 1
        for idx, row in enumerate(octopi):
            for idx2, num in enumerate(row):
                if num == -1:
                    continue
                if num == 9:
                    flashes.append([idx, idx2])
                octopi[idx][idx2] += 1

        # Then, look for flashes
        flashedThisRound = handleFlashes()
        flashed += flashedThisRound

        if partTwo and flashedThisRound == totalOctopi:
            break

        # Last, clear everyone that flashed this step
        for idx, row in enumerate(octopi):
            for idx2, col in enumerate(row):
                if col > 9:
                    octopi[idx][idx2] = 0
        i += 1

        if not partTwo and i == rounds + 1:
            break

    octopi = []
    return i if partTwo else flashed

def handleFlashes():
    global octopi, flashes
    flashed = len(flashes)

    while len(flashes) > 0:
        s = flashes.pop()
        x, y = [s[0], s[1]]
        neighbors = [
            [x + 1, y],
            [x - 1, y],
            [x, y + 1],
            [x, y - 1],
            [x + 1, y + 1],
            [x + 1, y - 1],
            [x - 1, y + 1],
            [x - 1, y - 1]
        ]

        for neighbor in neighbors:
            if octopi[neighbor[0]][neighbor[1]] != -1:
                octopi[neighbor[0]][neighbor[1]] += 1
                if octopi[neighbor[0]][neighbor[1]] == 10:
                    flashed += 1
                    flashes.append(neighbor)

    return flashed

def prettyPrintOctopi():
    for i in octopi:
        print(''.join(list(map(str, [j for j in i if j != -1]))))

if __name__ == "__main__":
    one = partOne(False)
    two = partOne(True)
    print(f"Part one: {one}")
    print(f"Part two: {two}")