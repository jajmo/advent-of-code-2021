INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def getInput():
    with open(INPUT_FILE, 'r') as f:
        inp = f.read().splitlines()

    template = list(inp[0])
    insertions = {}
    for i in inp[2:]:
        curr = i.split(' -> ')
        insertions[curr[0]] = curr[1]

    return [template, insertions]

def partOne():
    template, insertions = getInput()
    counter = 0
    steps = 10
    while counter < steps:
        place = 0
        while place < len(template) - 1:
            current = template[place] + template[place + 1]
            if current in insertions:
                place += 1
                template.insert(place, insertions[current])

            place += 1
        counter += 1

    letters = set(template)
    counts = [template.count(i) for i in list(letters)]
    return max(counts) - min(counts)

def partTwo():
    template, insertions = getInput()
    combinations = {}
    newCombinations = {}
    counter = 0
    steps = 40
    letterCounts = {}

    for i in insertions:
        combinations[i] = 0
        if insertions[i] not in letterCounts:
            letterCounts[insertions[i]] = 0

    while counter < len(template) - 1:
        combinations[template[counter] + template[counter + 1]] += 1
        counter += 1

    for i in template:
        letterCounts[i] += 1

    counter = 0
    while counter < steps:
        for combination in combinations:
            if combinations[combination] == 0:
                continue
            insertedLetter = insertions[combination]
            letterCounts[insertedLetter] += combinations[combination]
            firstCombination = combination[0] + insertedLetter
            secondCombination = insertedLetter + combination[1]

            newCombinations[firstCombination] = combinations[combination] if firstCombination not in newCombinations else newCombinations[firstCombination] + combinations[combination]
            newCombinations[secondCombination] = combinations[combination] if secondCombination not in newCombinations else newCombinations[secondCombination] + combinations[combination]

        combinations = newCombinations
        newCombinations = {}
        counter += 1

    maxV = minV = 0
    for i in letterCounts:
        maxV = letterCounts[i] if letterCounts[i] > maxV or maxV == 0 else maxV
        minV = letterCounts[i] if letterCounts[i] < minV or minV == 0 else minV

    return maxV - minV

if __name__ == "__main__":
    one = partOne()
    two = partTwo()
    print(f"Part one: {one}")
    print(f"Part two: {two}")