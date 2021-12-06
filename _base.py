INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()

    for line in lines:
        # Solution goes here

if __name__ == "__main__":
    main()