def getInput(f):
    start = None
    row = 0
    col = 0
    splitter = set()
    for line in f:
        line = line.strip()
        col = len(line)
        for c in range(0, len(line)):
            if line[c] == "S":
                start = c 
            elif line[c] == "^":
                splitter.add((row, c))
        row += 1
    return splitter, row, col, start



def getResult():
    f = open("7/input.txt", "r")
    # f = open("7/simple.txt", "r")
    total = 0
    splitter, row, col, start = getInput(f)
    beams = set([start])
    for bR in range(1, row):
        newBeams = set()
        for bC in beams:
            if (bR, bC) in splitter:
                total += 1
                if bC + 1 < col: 
                    newBeams.add(bC + 1)
                if bC - 1 >= 0:
                    newBeams.add(bC - 1)
            else:
                newBeams.add(bC)
        beams = newBeams
    return total

print(getResult())
# Solution 1658