INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()

    fish = list(map(int, lines[0].split(',')))

    for x in range(0, 80):
        fish.append(-1) # Mark where new fish start
        for i, j in enumerate(fish):
            if j == -1:
                del fish[i]
                break # Found new fish - stop this iteration
            if j > 0:
                fish[i] -= 1
            else:
                fish[i] = 6
                fish.append(8)

    print(len(fish))

if __name__ == "__main__":
    main()