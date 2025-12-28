f= open("1/input.txt", "r")
dirs = {'L': -1, 'R': 1}
currentNbr = 50
counter = 0
for line in f:
    dir = line[0]
    dis = int(line[1:])
    if currentNbr == 0:
        counter += dis // 100
    else:
        if dir == 'L':
            if currentNbr - dis <= 0:
                counter += 1
                disLeft = abs(dis - currentNbr)
                counter += (disLeft // 100)
        else:
            if currentNbr + dis >= 100:
                counter += 1
                disLeft = abs(dis  - (100 - currentNbr))
                counter += (disLeft // 100)
    currentNbr = (currentNbr + dis * dirs[dir]) % 100

print(counter)


# Solution 6892