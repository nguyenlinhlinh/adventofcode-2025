# Solved by setting up system equation or linear programing

import pulp
f = open("10/input.txt", "r")
# f = open("10/simple.txt", "r")

def parseInput():
    indicators = []
    buttons = []
    joltages = []
    for line in f:
        line = line.strip().split(" ")
        indicators.append([False if l == "." else True for l in line[0][1:-1]])
        buttons.append([[int(i) for i in l[1:-1].split(",")] for l in line[1:-1]])
        joltages.append([int(l) for l in line[-1][1:-1].split(",")])
    return buttons, joltages

def getResult():
    (buttons, joltages) = parseInput()
    total = 0
    for i in range(len(joltages)) :
        currJoltages = joltages[i]
        currButtons = buttons[i]
        prob = pulp.LpProblem("buttons", pulp.LpMinimize)
        x = [pulp.LpVariable(f"x{j}", lowBound=0, cat="Integer") for j in range(len(currButtons))]
        prob += pulp.lpSum(x)
        for j in range(len(currJoltages)):
            s = []
            for b in range(len(currButtons)):
                for joltageIndex in currButtons[b]:
                    if joltageIndex == j:
                        s.append(x[b])
            prob += pulp.lpSum(s) == currJoltages[j]
        prob.solve(pulp.PULP_CBC_CMD(msg=False))
        total += sum([int(var.value()) for var in x])    
    return total

print(getResult())

# Solution 21469