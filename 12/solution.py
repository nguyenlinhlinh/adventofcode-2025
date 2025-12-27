def getInput():
    regions = []
    f = open("12/input.txt", "r")
    # f = open("12/simple.txt", "r")
    for line in f:
        if line == '\n':
            continue
        line = line.strip()
        if "x" in line:
            [region, shapeList] = line.split(":")
            (col, row) = map(int, region.split("x"))
            nbrOfShapes = sum([int(i) for i in shapeList.strip().split(" ")])
            regions.append(((row, col), nbrOfShapes))
    return regions

def getResult():
    total = 0
    regions = getInput()
    for region, nbrOfShapes in regions:
        (row, col) = region
        if row // 3 * col // 3 >= nbrOfShapes:
            total += 1
    return total

print(getResult())

# Solution 599

