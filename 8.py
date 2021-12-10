INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()
    signals = []
    one = 2
    four = 4
    seven = 3
    eight = 7
    ones = fours = sevens = eights = 0

    for line in lines:
        line = line.split(" | ")
        signals.append([line[0].split(), line[1].split()])

    for signal in signals:
        for num in signal[1]:
            ones += 1 if len(num) == one else 0
            fours += 1 if len(num) == four else 0
            sevens += 1 if len(num) == seven else 0
            eights += 1 if len(num) == eight else 0

    print(ones + fours + sevens + eights)

if __name__ == "__main__":
    main()