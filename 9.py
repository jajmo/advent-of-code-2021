INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"
locations = []
def getInput():
    with open(INPUT_FILE, 'r') as f:
        return f.read().splitlines()

def partOne():
    inp = getInput()
    locations = []

    # cheating by surrounding the matrix in 20s to avoid bounds errors
    locations.append([20] * (len(inp[0]) + 2))
    for line in inp:
        locations.append([20] + list(map(int, list(line))) + [20])
    locations.append([20] * (len(inp[0]) + 2))

    risk = 0

    for idx, row in enumerate(locations):
        for idx2, val in enumerate(row):
            if (val < locations[idx - 1][idx2] and val < locations[idx + 1][idx2] and
                val < locations[idx][idx2 - 1] and val < locations[idx][idx2 + 1]):
                risk += val + 1

    return risk

def partTwo():
    inp = getInput()

    # cheating by surrounding the matrix in 20s to avoid bounds errors
    locations.append([20] * (len(inp[0]) + 2))
    for line in inp:
        locations.append([20] + list(map(int, list(line))) + [20])
    locations.append([20] * (len(inp[0]) + 2))

    lowPoints = []

    for idx, row in enumerate(locations):
        for idx2, val in enumerate(row):
            if (val < locations[idx - 1][idx2] and val < locations[idx + 1][idx2] and
                val < locations[idx][idx2 - 1] and val < locations[idx][idx2 + 1]):
                lowPoints.append([idx, idx2])

    mult = 1
    sizes = []
    for point in lowPoints:
        sizes.append(getBasinSize(point[0], point[1]))

    sizes = sorted(sizes)[-3:]
    for i in sizes:
        mult *= i

    return mult

# literally just bfs
def getBasinSize(point1, point2):
    visited = []
    queue = []
    basinSize = 0

    queue.append([point1, point2])

    while len(queue) > 0:
        s = queue.pop()
        neighbors = getNeighbors(s)
        for neighbor in neighbors:
            if neighbor not in visited and locations[neighbor[0]][neighbor[1]] < 9:
                basinSize += 1
                visited.append(neighbor)
                queue.append(neighbor)

    return basinSize

def getNeighbors(point):
    x, y = point
    return [
        [x + 1, y],
        [x - 1, y],
        [x, y + 1],
        [x, y - 1]
    ]

if __name__ == "__main__":
    one = partOne()
    two = partTwo()
    print(f"Part one: {one}")
    print(f"Part two: {two}")