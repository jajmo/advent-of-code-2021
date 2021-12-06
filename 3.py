INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()
        count = len(lines)
        width = len(lines[0])
        ones = zeros = row = col = 0
        gamma = epsilon = ""

        while col < width:
            while row < count:
                bit = int(lines[row][col])
                if bit == 0:
                    zeros += 1
                else:
                    ones += 1
                row += 1

            gamma += "1" if ones > zeros else "0"
            epsilon += "1" if zeros > ones else "0"
            row = zeros = ones = 0
            col += 1

        gammaDec = int(gamma, 2)
        epsilonDec = int(epsilon, 2)
        power = gammaDec * epsilonDec

        print(f"Power: {power}")


if __name__ == "__main__":
    main()