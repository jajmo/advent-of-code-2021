INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

class Packet:
    def __init__(self, version, typeID, number = None):
        self.version = version
        self.type = typeID
        self.number = number
        self.children = []

def getInput():
    with open(INPUT_FILE, 'r') as f:
        inp = f.read().splitlines()

    return ''.join(bin(int(i, 16))[2:].zfill(4) for i in inp[0])

def partOne():
    inp = getInput()
    root = Packet(0, None)
    parsePacket(inp, 0, root)
    return packetVersionSum(root)

def partTwo():
    inp = getInput()
    root = Packet(0, None)
    parsePacket(inp, 0, root)
    return doOperations(root)

def parseOperatorPacket(inp, start, parent):
    loc = start
    lengthType = int(inp[loc + 6], 2)
    version = int(inp[loc:loc + 3], 2)
    typeID = int(inp[loc + 3:loc + 6], 2)
    root = Packet(version, typeID)
    parent.children.append(root)

    if lengthType == 0:
        totalPacketLength = int(inp[loc + 7:loc + 22], 2)
        loc += 22
        while loc < totalPacketLength + start + 22:
            loc = parsePacket(inp, loc, root)
    else:
        totalPackets = int(inp[loc + 7:loc + 18], 2)
        loc += 18
        for i in range(totalPackets):
            loc = parsePacket(inp, loc, root)

    return loc

def parseLiteralPacket(inp, start, parent):
    num = ''
    loc = start + 6
    i = loc
    while True:
        num += str(inp[i + 1:i + 5])
        loc += 5
        if inp[i] == '0':
            break

        i += 5

    parent.children.append(Packet(int(inp[start:start + 3], 2), 4, int(num, 2)))
    return loc

def parsePacket(inp, start, parent):
    typeID = int(inp[start + 3:start + 6], 2)
    if typeID == 4:
        return parseLiteralPacket(inp, start, parent)
    else:
        return parseOperatorPacket(inp, start, parent)

def packetVersionSum(packet):
    s = 0
    queue = [packet]

    while len(queue) != 0:
        curr = queue.pop(0)
        s += curr.version

        for i in curr.children:
            queue.append(i)

    return s

def doOperations(node):
    if node.type == None: # Root node, has one child
        return doOperations(node.children[0])

    if node.type == 0:
        return doOperations(node.children[0]) if len(node.children) == 1 else sum(list(map(doOperations, node.children)))
    elif node.type == 1:
        if len(node.children) == 1:
            return doOperations(node.children[0])
        else:
            prod = 1
            for i in node.children:
                prod *= doOperations(i)
            return prod
    elif node.type == 2:
        return min(list(map(doOperations, node.children)))
    elif node.type == 3:
        return max(list(map(doOperations, node.children)))
    elif node.type == 4:
        return node.number
    elif node.type == 5:
        return 1 if doOperations(node.children[0]) > doOperations(node.children[1]) else 0
    elif node.type == 6:
        return 1 if doOperations(node.children[0]) < doOperations(node.children[1]) else 0
    elif node.type == 7:
        return 1 if doOperations(node.children[0]) == doOperations(node.children[1]) else 0

if __name__ == "__main__":
    one = partOne()
    two = partTwo()
    print(f"Part one: {one}")
    print(f"Part two: {two}")
