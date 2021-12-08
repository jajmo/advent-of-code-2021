from statistics import median

INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()

    crabs = list(map(int, lines[0].split(',')))
    mid = int(median(crabs))
    print(sum(list(map(lambda x: abs(x - mid), crabs))))

if __name__ == "__main__":
    main()