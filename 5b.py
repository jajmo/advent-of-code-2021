INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()

    maxX = maxY = 0
    graph = []

    # First we need to figure out the dimensions of the final array
    for line in lines:
        line = line.split(" -> ")
        y1 = int(line[0].split(',')[0])
        y2 = int(line[1].split(',')[0])
        x1 = int(line[0].split(',')[1])
        x2 = int(line[1].split(',')[1])
        x1 = x1 if x1 > x2 else x2
        y1 = y1 if y1 > y2 else y2
        maxX = maxX if maxX > x1 else x1
        maxY = maxY if maxY > y1 else y1
    
    # Then we create the graph with all dots for untraversed items
    for i in range(0, maxY + 1):
        graph.insert(i, ['.'] * (maxX + 1))

    # Then we figure out what crosses where
    for line in lines:
        line = line.split(" -> ")
        y1 = int(line[0].split(',')[0])
        y2 = int(line[1].split(',')[0])
        x1 = int(line[0].split(',')[1])
        x2 = int(line[1].split(',')[1])

        if x1 == x2:
            for i in myRange(min(y1, y2), max(y1, y2)):
                graph[x1][i] = 1 if graph[x1][i] == "." else graph[x1][i] + 1
        elif y1 == y2:
            for i in myRange(min(x1, x2), max(x1, x2)):
                graph[i][y1] = 1 if graph[i][y1] == "." else graph[i][y1] + 1
        else:
            i = x1
            j = y1
            xBound = x2 + 1 if x1 < x2 else x2 - 1
            yBound = y2 + 1 if y1 < y2 else y2 - 1
            while i != xBound and j != yBound:
                graph[i][j] = 1 if graph[i][j] == "." else graph[i][j] + 1
                i = i + 1 if x1 < x2 else i - 1
                j = j + 1 if y1 < y2 else j - 1

    overlaps = 0
    for row in graph:
        for col in row:
            if col != "." and col > 1:
                overlaps += 1
    print(overlaps)


def prettyPrint(array):
    for i in array:
        print("".join(map(str, i)))

def myRange(start, stop):
    out = []
    for i in range(start, stop + 1):
        out.append(i)
    return out

if __name__ == "__main__":
    main()