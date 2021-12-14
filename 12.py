INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def getInput():
    with open(INPUT_FILE, 'r') as f:
        return f.read().splitlines()

def partOne(partTwo = False):
    inp = getInput()
    graph = {}

    for line in inp:
        line = line.split('-')
        if line[0] in graph:
            graph[line[0]].append(line[1])
        else:
            graph[line[0]] = [line[1]]

        if line[1] in graph:
            graph[line[1]].append(line[0])
        else:
            graph[line[1]] = [line[0]]

    paths = 0
    for node in graph['start']:
        paths+= len(traverse(node, graph, ['start'], partTwo))

    return paths

def traverse(start, graph, path, partTwo):
    path = path + [start]
    if start == 'end':
        return [path]

    paths = []
    for node in graph[start]:
        if node == 'start':
            continue
        if node.isupper() or (node.islower() and ((node not in path) or (partTwo and lowerCounts(path) == 0))):
            for p in traverse(node, graph, path, partTwo):
                paths.append(p)
    return paths

def lowerCounts(path):
    counts = {}
    lowers = 0

    for i in path:
        if i.isupper():
            continue

        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    for k in counts:
        if counts[k] > 1:
            lowers += 1

    return lowers

def pp(arr):
    for i in arr:
        print(i)

if __name__ == "__main__":
    one = partOne(False)
    two = partOne(True)
    print(f"Part one: {one}")
    print(f"Part two: {two}")