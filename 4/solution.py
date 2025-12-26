f = open("4/input.txt", "r")
# f = open("4/simple.txt", "r")
total = 0
dirs = [(-1,-1), (-1,0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
grid = set()
row = 0
for line in f:
    line = line.strip()
    for col in range(len(line)):
        if line[col] == '@':
            grid.add((row, col))
    row += 1

def isInsideGrid(r, c, grid):
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

for (r, c) in grid:
    rolls = 0
    for (aR, aC) in dirs:
        if (r + aR, c + aC) in grid:
            rolls += 1
    if rolls < 4:
        total += 1

print(total)

# Solution 1478