f = open("1/input.txt", "r")
currentNbr = 50
counter = 0
dirs = {'L': -1, 'R': 1}
for line in f:
    dir = line[0]
    dis = int(line[1:])
    currentNbr = (currentNbr - dis * dirs[dir]) % 100
    if currentNbr == 0:    
        counter += 1
print(counter)

# Solution 1180