import re

INPUT_FILE = f"input/{__file__.split('.')[0].rstrip('b')}"

def getInput():
    with open(INPUT_FILE, 'r') as f:
        inp = f.read().splitlines()

    l = re.split("[x|y]=", inp[0])
    x = list(map(int, l[1].rstrip(', ').split("..")))
    y = list(map(int, l[2].split("..")))

    return [x, y]

def partOne(partTwo = False):
    inTargetArea = 0
    x, y = getInput()
    maxY = maxYGlobal = 0
    xVel = yVel = 1

    for xVelOrig in range(x[1] + 10):
        for yVelOrig in range(y[0], abs(y[0])):
            maxY = 0
            xVel = xVelOrig
            yVel = yVelOrig
            pos = [0, 0]

            while True:
                if yVel > 0:
                    maxY += yVel

                # Step forward
                pos[0] += xVel
                pos[1] += yVel
                xVel = xVel - 1 if xVel > 0 else xVel
                yVel -= 1

                # Are we in the target zone?
                if pos[0] >= x[0] and pos[0] <= x[1] and pos[1] >= y[0] and pos[1] <= y[1]:
                    inTargetArea += 1

                    # If we are, check if our iteration's maxY is greater than the global maxY
                    if maxY > maxYGlobal:
                        maxYGlobal = maxY
                    break

                # Out of bounds
                if pos[0] > x[1] or pos[1] < y[0]:
                    break

    return inTargetArea if partTwo else maxYGlobal

if __name__ == "__main__":
    one = partOne()
    two = partOne(True)
    print(f"Part one: {one}")
    print(f"Part two: {two}")