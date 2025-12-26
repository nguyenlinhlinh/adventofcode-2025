def getInput(file):
    ranges = []
    for line in file:
        if line == '\n':
            break
        r = line.strip().split("-")
        ranges.append((int(r[0]), int(r[1])))
    return ranges

def mergeRanges(ranges):
    ranges.sort(key=lambda a:a[0])
    mergedRanges = [ranges[0]]
    for i in range(1, len(ranges)):
        (start, end) = ranges[i]
        # Half inside
        if start <= mergedRanges[-1][1] and end > mergedRanges[-1][1]:
            mergedRanges.append((mergedRanges[-1][1]+ 1, end))
        # Lay outside
        elif start > mergedRanges[-1][1]:
            mergedRanges.append((start, end))
    return mergedRanges

def getResult():
    f = open("5/input.txt", "r")
    # f = open("5/simple.txt", "r")
    ranges = getInput(f)
    mergedRanges = mergeRanges(ranges)
    total = 0
    for s, e in mergedRanges:
        total += (e - s + 1)
    return total

print(getResult())

# Solution 359913027576322