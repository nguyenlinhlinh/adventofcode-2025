# Count the number of clicks in two cases:
# Already at 0 then how many clicks are pointing at 0 using modulo
# At other numbers then count how many click from this number to reach 0. 
# When it is at 0 again just count how many times it points at 0 using modul0.
f= open("1/input.txt", "r")
dirs = {'L': -1, 'R': 1}
currentNbr = 50
counter = 0
for line in f:
    dir = line[0]
    dis = int(line[1:])
    if dir == 'L':
        if currentNbr == 0:
            counter += dis // 100
        elif currentNbr - dis <= 0:
            counter += 1
            disLeft = abs(dis - currentNbr)
            counter += (disLeft // 100)
    else:
        if currentNbr == 0:
            counter += dis // 100
        elif currentNbr + dis >= 100:
            counter += 1
            disLeft = abs(dis  - (100 - currentNbr))
            counter += (disLeft // 100)
    currentNbr = (currentNbr + dis * dirs[dir]) % 100

print(counter)


# Solution 6892