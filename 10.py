from statistics import median

INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def getInput():
    with open(INPUT_FILE, 'r') as f:
        return f.read().splitlines()

def partOne():
    inp = getInput()
    total = 0
    opens = "([{<"
    closes = ")]}>"
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    for line in inp:
        brackets = []
        for char in line:
            if char in opens:
                brackets.append(char)
            else:
                closed = brackets.pop()
                if opens.index(closed) != closes.index(char):
                    total += points[char]
                    break

    return total

def partTwo():
    inp = getInput()
    scores = []
    opens = "([{<"
    closes = ")]}>"
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    for line in inp:
        corrupt = False
        total = 0
        brackets = []
        for char in line:
            if char in opens:
                brackets.append(char)
            else:
                closed = brackets.pop()
                if opens.index(closed) != closes.index(char):
                    corrupt = True
                    break

        if corrupt:
            continue

        brackets = reversed(brackets)
        for char in brackets:
            total *= 5
            total += points[closes[opens.index(char)]]

        scores.append(total)

    return median(scores)

if __name__ == "__main__":
    one = partOne()
    two = partTwo()
    print(f"Part one: {one}")
    print(f"Part two: {two}")