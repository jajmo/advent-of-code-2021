INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"
known_by_length = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.read().splitlines()
    total = 0

    for line in lines:
        line = line.split(" | ")
        signal_patterns, digits = line[0].split(), line[1].split()
        total += decode(signal_patterns, digits)

    print(total)

# cheated again
def decode(signal_patterns, digits):
    signal_patterns = [''.join(sorted(pattern)) for pattern in signal_patterns]
    digits = [''.join(sorted(digit)) for digit in digits]

    mapping = {}
    reverse_mapping = {}

    for pattern in signal_patterns:
        pattern_length = len(pattern)

        if (pattern_length in known_by_length): # 1, 4, 7, 8
            pattern_number = known_by_length[pattern_length]
            mapping[pattern] = pattern_number
            reverse_mapping[pattern_number] = set(pattern)
    
    for pattern in signal_patterns:
        pattern_length = len(pattern)
        pattern_set = set(pattern)

        if (pattern_length == 6): # 0, 6, 9
            if (not reverse_mapping[1].issubset(pattern_set)):
                mapping[pattern] = 6
            elif (reverse_mapping[4].issubset(pattern_set)):
                mapping[pattern] = 9
            else:
                mapping[pattern] = 0
        elif (pattern_length == 5): # 2, 3, 5
            if (reverse_mapping[1].issubset(pattern_set)):
                mapping[pattern] = 3
            elif ((reverse_mapping[4] | pattern_set) == reverse_mapping[8]):
                mapping[pattern] = 2
            else:
                mapping[pattern] = 5   

    return int(''.join([str(mapping[digit]) for digit in digits]))

if __name__ == "__main__":
    main()