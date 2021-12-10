INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()
    locations = []

    # cheating by surrounding the matrix in 20s to avoid bounds errors
    locations.append([20] * (len(lines[0]) + 2))
    for line in lines:
        locations.append([20] + list(map(int, list(line))) + [20])
    locations.append([20] * (len(lines[0]) + 2))

    risk = 0

    for idx, row in enumerate(locations):
        for idx2, val in enumerate(row):
            if (val < locations[idx - 1][idx2] and val < locations[idx + 1][idx2] and
                val < locations[idx][idx2 - 1] and val < locations[idx][idx2 + 1]):
                risk += val + 1

    print(risk)

if __name__ == "__main__":
    main()