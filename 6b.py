INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def main():
    fish = dict()
    days = 80
    with open(INPUT_FILE,"r") as infile:
        counters = [ int(x) for x in infile.read().strip().split(',') ]

    # cheated from reddit
    for i in range(9):
        fish[i] = counters.count(i)
    for i in range(256):
        fish[(i+7)%9] += fish[i%9]

    print(sum(fish.values()))

if __name__ == "__main__":
    main()