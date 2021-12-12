INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def getInput():
    with open(INPUT_FILE, 'r') as f:
        return f.read().splitlines()

def partOne():
    inp = getInput()
    fish = list(map(int, inp[0].split(',')))

    for x in range(0, 80):
        fish.append(-1) # Mark where new fish start
        for i, j in enumerate(fish):
            if j == -1:
                del fish[i]
                break # Found new fish - stop this iteration
            if j > 0:
                fish[i] -= 1
            else:
                fish[i] = 6
                fish.append(8)

    return len(fish)


def partTwo():
    inp = getInput()
    fish = dict()
    days = 80
    counters = [ int(x) for x in inp[0].split(',') ]

    # cheated from reddit
    for i in range(9):
        fish[i] = counters.count(i)
    for i in range(256):
        fish[(i+7)%9] += fish[i%9]

    return sum(fish.values())

if __name__ == "__main__":
    one = partOne()
    two = partTwo()
    print(f"Part one: {one}")
    print(f"Part two: {two}")