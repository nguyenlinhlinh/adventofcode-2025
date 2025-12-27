import math

def getInput(f):
    coordinates = []
    for line in f:
        line = line.strip()
        coordinates.append([int(i) for i in line.split(",")])
    return coordinates

def getDistance(a, b, coordinates):
    [x1, y1, z1] = coordinates[a] 
    [x2, y2, z2] = coordinates[b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 )    

def getDistances(coordinates):
    distances = []
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            d = getDistance(i, j, coordinates)
            distances.append((d, i , j))
    return distances


def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)
    return parents[x]

def union(a, b, size, parents):
    rootA = find(a, parents)
    rootB = find(b, parents)
    if rootA != rootB:
        parents[rootA] = rootB
        size[rootB] += size[rootA]
        return True
    else:
        return False

def getResult():
    f = open("8/input.txt", "r")
    # f = open("8/simple.txt", "r")
    coordinates = getInput(f)
    N = len(coordinates)
    parents = [i for i in range(N)]
    size = [1] * N
    distances = getDistances(coordinates)
    distances.sort()
    connectedComp = N
    i = 0
    while connectedComp > 1:
        _, a , b = distances[i]
        if union(a, b, size, parents):
            connectedComp -=1
        i += 1
    (_, a, b) = distances[i - 1]
    return coordinates[a][0]*coordinates[b][0]

print(getResult())

# Solution 7893123992