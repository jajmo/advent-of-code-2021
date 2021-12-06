INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        increasing = firstSum = secondSum = place = 0
        total = len(lines)

        while place < total - 2:
            val = int(lines[place].strip()) + int(lines[place + 1].strip()) + int(lines[place + 2].strip())
            if firstSum == 0:
                firstSum = val
            else:
                secondSum = val

            if firstSum != 0 and secondSum != 0:
                if secondSum > firstSum:
                    increasing += 1

                firstSum = secondSum
                secondSum = 0

            place += 1

    print(increasing)

if __name__ == "__main__":
    main()