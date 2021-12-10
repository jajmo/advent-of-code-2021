INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()

    total = 0
    opens = "([{<"
    closes = ")]}>"
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    for line in lines:
        brackets = []
        for char in line:
            if char in opens:
                brackets.append(char)
            else:
                closed = brackets.pop()
                if opens.index(closed) != closes.index(char):
                    total += points[char]
                    break

    print(total)

if __name__ == "__main__":
    main()