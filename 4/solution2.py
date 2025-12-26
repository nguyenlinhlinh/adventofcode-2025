f = open("4/input.txt", "r")
# f = open("4/simple.txt", "r")
total = 0
dirs = [(-1,-1), (-1,0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
grid = []
row = 0
for line in f:
    line = line.strip()
    for col in range(len(line)):
        if line[col] == '@':
            grid.append((row, col))
    row += 1
while True:
    previous = total
    positions = set(grid)
    for (r, c) in grid:
        if (r, c ) not in positions:
            continue
        rolls = 0
        for (aR, aC) in dirs:
            if (r + aR, c + aC) in positions:
                rolls += 1
        if rolls < 4:
            total += 1
            positions.remove((r, c))

    grid = list(positions)
    if previous == total:
        break
            

print(total)

# Solution 9120
