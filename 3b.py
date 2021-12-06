INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()
    

    oxygen = processList(lines, True)
    co2 = processList(lines, False)

    print(oxygen)
    print(co2)

def getNumbers(lines, bit, pos, includeOnes, includeZeros):
    numbers = []
    for line in lines:
        if (includeOnes == True and int(line[pos]) == 1) or (includeZeros == True and int(line[pos]) == 0) or (includeOnes == False and includeZeros == False and  int(line[pos]) == int(bit)):
            numbers.append(line)

    return numbers

def processList(lines, commonOnly):
    count = len(lines)
    width = len(lines[0])
    ones = zeros = row = col = 0

    while col < width:
        while row < count:
            bit = int(lines[row][col])
            if bit == 0:
                zeros += 1
            else:
                ones += 1
            row += 1

        common = 1 if ones > zeros else 0
        notCommon = 1 if zeros > ones else 0

        lines = getNumbers(lines, common if commonOnly else notCommon, col, ones == zeros and commonOnly, ones == zeros and not commonOnly)
        if len(lines) > 1:
            zeros = ones = row = 0
            col += 1
        else:
            break

        count = len(lines)
        width = len(lines[0])

    return int(lines[0], 2)


if __name__ == "__main__":
    main()