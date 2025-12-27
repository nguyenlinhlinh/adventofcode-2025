from collections import defaultdict
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
                start = (row, c) 
            elif line[c] == "^":
                splitter.add((row, c))
        row += 1
    return splitter, row, col, start

def BFS(splitter, row, col, start):
    beams = [start]
    visited = set()
    endpos = defaultdict(int)
    endpos[start] = 1
    total = 0
    while beams:
        (bR, bC) = beams.pop(0)
        if (bR, bC) in visited:
            continue
        visited.add((bR, bC))
        if bR + 1 < row:
            if (bR+1, bC) in splitter:
                if bC + 1 < col:
                    if (bR + 1, bC - 1) not in visited:
                        beams.append((bR + 1, bC - 1))
                    endpos[(bR + 1, bC - 1)] += endpos[(bR, bC)]
                if bC - 1 < col:
                    if (bR + 1, bC + 1) not in visited:
                        beams.append((bR + 1, bC +1))
                    endpos[(bR + 1, bC + 1)] += endpos[(bR, bC)]
            else:
                beams.append((bR + 1, bC))
                endpos[(bR + 1, bC)] += endpos[(bR, bC)]

        else:
            total += endpos[(bR, bC)]

    return total

def getResult():
    f = open("7/input.txt", "r")
    # f = open("7/simple.txt", "r")
    splitter, row, col, start = getInput(f)
    return BFS(splitter, row, col, start)

print("total", getResult())
# Solution 53916299384254