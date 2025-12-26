f = open("5/input.txt", "r")
# f = open("5/simple.txt", "r")
total = 0
ranges = []
checkFood = False
for line in f:
    if "-" in line:
        r = line.strip().split("-")
        ranges.append((int(r[0]), int(r[1])))
    elif line != '\n':
        id = int(line.strip())
        for x, y in ranges:
            if id >= x and id <= y:
                total += 1
                break
print(total)

# Solution 840

