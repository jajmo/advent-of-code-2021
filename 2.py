INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def getInput():
    with open(INPUT_FILE, 'r') as f:
        return f.read().splitlines()

def partOne():
    inp = getInput()
    horizontal = depth = 0

    for line in inp:
        line = line.strip().split(' ')

        if line[0] == "forward":
            horizontal += int(line[1])
        elif line[0] == "down":
            depth += int(line[1])
        elif line[0] == "up":
            depth -= int(line[1])

    return horizontal * depth


def partTwo():
    inp = getInput()
    horizontal = depth = aim = 0

    for line in inp:
        line = line.strip().split(' ')

        if line[0] == "forward":
            horizontal += int(line[1])
            depth += (aim * int(line[1]))
        elif line[0] == "down":
            aim += int(line[1])
        elif line[0] == "up":
            aim -= int(line[1])

    return horizontal * depth

if __name__ == "__main__":
    one = partOne()
    two = partTwo()
    print(f"Part one: {one}")
    print(f"Part two: {two}")