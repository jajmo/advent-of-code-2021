from statistics import median

INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()

    crabs = list(map(int, lines[0].split(',')))
    it = range(max(crabs))
    minTotalFuel = 0

    for i in it:
        fuel = 0
        for j in crabs:
            distance = abs(i - j)
            fuel += sum(range(distance + 1))
        if minTotalFuel == 0 or fuel < minTotalFuel:
            minTotalFuel = fuel
    print(minTotalFuel)

if __name__ == "__main__":
    main()