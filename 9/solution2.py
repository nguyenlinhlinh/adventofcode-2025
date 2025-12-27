import sys

def getInput(f):
    coordinates = []
    for line in f:
        x, y = map(int, line.strip().split(","))
        coordinates.append((x, y))
    return coordinates

def getXRanges(coordinates):
    N = len(coordinates)
    xRanges = []
    coordinates.sort(key=lambda a:a[1])
    start = 0
    while start < N:
        currentY = coordinates[start][1]
        end = start+1
        while end < N and coordinates[end][1] == currentY:
            end +=1
        r = sorted(coordinates[start: end], key=lambda a: a[0])
        xRanges.append((currentY, r[0][0], r[-1][0]))
        start = end
    xRanges.sort()
    return xRanges


def getYRanges(coordinates):
    N = len(coordinates)
    yRanges = []
    coordinates.sort(key=lambda a:a[0])
    start = 0
    while start < N:
        currentX = coordinates[start][0]
        end = start+1
        while end < N and coordinates[end][0] == currentX:
            end +=1
        r = sorted(coordinates[start: end], key=lambda a: a[1])
        yRanges.append((currentX, r[0][1], r[-1][1]))
        start = end
    yRanges.sort()
    return yRanges



def mergeRange(r):
    if not r:
        return []
    r.sort()
    merged = [r[0]]
    for i in range(1, len(r)):
        (s, e) = r[i]
        if merged[-1][1] > e:
            continue
        elif merged[-1][1] > s:
            merged[-1] = (merged[-1][0], e)
        elif merged[-1][1] == s:
            merged[-1] = (merged[-1][0], e)
        else:
            merged.append((s, e))
    return merged

def isInXRange(s, e, sy, ey, xRanges):
    check = [False for i in range(2)]
    lessThanYRange = []
    greaterThanYRange = []
    for currY, sx, ex in xRanges:
        if currY <= sy:
            lessThanYRange.append((sx, ex))
        if currY >= ey:
            greaterThanYRange.append((sx, ex))
    lessThanYRange = mergeRange(lessThanYRange)
    greaterThanYRange = mergeRange(greaterThanYRange)
    for r in lessThanYRange:
        if r[0] <= s and e <= r[1]:
            check[0] = True
    for r in greaterThanYRange:
        if r[0] <= s and e <= r[1]:
            check[1] = True
    
    return check[0] and check[1]


def isInYRange(s, e, sx, ex, yRanges):
    check = [False for i in range(2)]
    lessThanXRange = []
    greaterThanXRange = []
    for currX, sy, ey in yRanges:
        if currX <= sx:
            lessThanXRange.append((sy, ey))
        if currX >= ex:
            greaterThanXRange.append((sy, ey))
    lessThanXRange = mergeRange(lessThanXRange)
    greaterThanXRange = mergeRange(greaterThanXRange)
    for r in lessThanXRange:
        if r[0] <= s and e <= r[1]:
            check[0] = True
    for r in lessThanXRange:
        if r[0] <= s and e <= r[1]:
            check[1] = True
    
    return check[0] and check[1]

def getResult():
    # f = open("9/simple.txt", "r")
    f = open("9/input.txt", "r")
    coordinates = getInput(f)
    N = len(coordinates)
    coordinates.sort()
    largest = 0
    xRanges = getXRanges(coordinates)
    yRanges = getYRanges(coordinates)
    for i in range(N):
        for j in range(i +1, N):
            (x1, y1) = coordinates[i]
            (x2, y2) = coordinates[j]

            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area < largest:
                continue
            yR = [y1, y2]
            yR.sort()
            if isInXRange(x1, x2, yR[0], yR[1], xRanges) and isInYRange(yR[0], yR[1], x1, x2, yRanges):
                largest = area
    return largest

                        

print("largest", getResult())
# Solution 1537458069