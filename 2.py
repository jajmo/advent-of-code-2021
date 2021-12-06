INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        horizontal = depth = 0

        for line in lines:
            line = line.strip().split(' ')

            if line[0] == "forward":
                horizontal += int(line[1])
            elif line[0] == "down":
                depth += int(line[1])
            elif line[0] == "up":
                depth -= int(line[1])

        print(f'Horizontal: {horizontal}')
        print(f'Depth:      {depth}')

if __name__ == "__main__":
    main()