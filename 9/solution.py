import math
f = open("9/input.txt", "r")
# f = open("9/simple.txt", "r")
largest = 0
coordinates = []
for line in f:
    x, y = map(int, line.strip().split(","))
    coordinates.append((x, y))
N = len(coordinates)
for i in range(N):
    (x1, y1) = coordinates[i]
    for j in range(N):
        if i == j:
            continue
        (x2, y2) = coordinates[j]
        deltaX = abs(x2 - x1 + 1)
        deltaY = abs(y2 - y1 + 1)
        largest = max(largest, deltaX * deltaY)
print(largest)
# Solution 4735268538