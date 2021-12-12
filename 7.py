from statistics import median

INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"
    
def getInput():
    with open(INPUT_FILE, 'r') as f:
        return f.read().splitlines()

def partOne():
    inp = getInput()
    crabs = list(map(int, inp[0].split(',')))
    mid = int(median(crabs))
    return sum(list(map(lambda x: abs(x - mid), crabs)))

def partTwo():
    inp = getInput()
    crabs = list(map(int, inp[0].split(',')))
    it = range(max(crabs))
    minTotalFuel = 0

    for i in it:
        fuel = 0
        for j in crabs:
            distance = abs(i - j)
            fuel += sum(range(distance + 1))
        if minTotalFuel == 0 or fuel < minTotalFuel:
            minTotalFuel = fuel
    return minTotalFuel

if __name__ == "__main__":
    one = partOne()
    two = partTwo()
    print(f"Part one: {one}")
    print(f"Part two: {two}")