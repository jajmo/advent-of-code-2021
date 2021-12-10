from statistics import median

INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()

    scores = []
    opens = "([{<"
    closes = ")]}>"
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    for line in lines:
        corrupt = False
        total = 0
        brackets = []
        for char in line:
            if char in opens:
                brackets.append(char)
            else:
                closed = brackets.pop()
                if opens.index(closed) != closes.index(char):
                    corrupt = True
                    break

        if corrupt:
            continue

        brackets = reversed(brackets)
        for char in brackets:
            total *= 5
            total += points[closes[opens.index(char)]]

        scores.append(total)

    print(median(scores))


if __name__ == "__main__":
    main()