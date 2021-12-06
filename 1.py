INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        prev = int(lines[0].strip())
        increasing = 0

        for line in lines:
            line = int(line.strip())
            if line > prev:
                increasing += 1
            prev = line

    print(increasing)

if __name__ == "__main__":
    main()