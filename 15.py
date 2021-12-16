import heapq

INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def getInput(zeros = True):
    with open(INPUT_FILE, 'r') as f:
        inp = f.read().splitlines()
    data = []

    if zeros:
        data.append([-1] * (len(inp[0]) + 2))
    for i in inp:
        if zeros:
            data.append([-1] + list(map(int, list(i))) + [-1])
        else:
            data.append(list(map(int, list(i))))

    if zeros:
        data.append([-1] * (len(inp[0]) + 2))

    return data

def partOne():
    inp = getInput()
    return getMinCost(inp)
    
def partTwo():
    inp = getInput(False)
    newInp = []
    maxWidth = len(inp[0])
    maxHeight = len(inp)

    for i in range(maxHeight * 5):
        newInp.append([])
        for j in range(maxWidth * 5):
            newInp[i].append([])
            newInp[i][j] = inp[i % maxHeight][j % maxWidth]

    inp = newInp
    iterHeight = len(inp)
    iterWidth = len(inp[0])
    incr = incj = 0

    for i in range(iterHeight):
        if i > 0 and  i % maxHeight == 0:
            incr += 1

        incj = 0

        for j in range(iterWidth):
            if j > 0 and  j % maxWidth == 0:
                incj += 1

            inp[i][j] = inp[i][j] + incr + incj
            inp[i][j] = inp[i][j] if inp[i][j] < 10 else inp[i][j] - 9

    for i, j in enumerate(inp):
        inp[i] = [-1] + j + [-1]

    inp.insert(0, [-1] * len(inp[0]))
    inp.append([-1] * len(inp[0]))

    return getMinCost(inp)

def getMinCost(inp):
    end = [len(inp) - 2, len(inp[0]) - 2]
    queue, visited = [(0, [1, 1], [])], []
    heapq.heapify(queue)

    while len(queue) > 0:
        cost, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.append(node)
            path = path + [node]
            if node == end:
                return cost

            for c, neighbor in getNeighbors(node, inp):
                if c == -1:
                    continue
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + c, neighbor, path))

    return 0


def getNeighbors(node, graph):
    y, x = node
    return [
        [graph[y + 1][x], [y + 1, x]],
        [graph[y - 1][x], [y - 1, x]],
        [graph[y][x + 1], [y, x + 1]],
        [graph[y][x - 1], [y, x - 1]]
    ]

def pp(arr):
   for i in arr:
    print(''.join([str(j) for j in i]))

if __name__ == "__main__":
    one = partOne()
    two = partTwo()
    print(f"Part one: {one}")
    print(f"Part two: {two}")