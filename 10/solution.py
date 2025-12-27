def getInput(f):
    indicators = []
    buttons = []
    joltages = []
    for line in f:
        line = line.strip().split(" ")
        indicators.append([False if l == "." else True for l in line[0][1:-1]])
        buttons.append([[int(i) for i in l[1:-1].split(",")] for l in line[1:-1]])
    return indicators, buttons

def bfs(expected, buttons):
    state = [False for i in range(len(expected))]
    visited = set()
    queue = [(state, 0)]
    while len(queue):
        (currentState, totalPresses) = queue.pop(0)
        endState = True
        for i in range(len(expected)):
            if currentState[i] != expected[i]:
                endState = False
                break
        if endState:
            return totalPresses
        if str(currentState) in visited:
            continue
        visited.add(str(currentState))
        for button in buttons:
            newState = [i for i in currentState]
            for i in button:
                newState[i] = not newState[i]
                if str(newState) not in visited:
                    queue.append((newState, totalPresses + 1))

def getResult():
    f = open("10/input.txt", "r")
    # f = open("10/simple.txt", "r")
    indicators, buttons = getInput(f)
    total = 0
    for i in range(len(indicators)):
        total += bfs(indicators[i], buttons[i])
    return total

print(getResult())

# Solution 517

