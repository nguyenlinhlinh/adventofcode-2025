f = open("11/input.txt", "r")
# f = open("11/simple.txt", "r")
total = 0
nodes = {}
for line in f:
    line = line.strip()
    [node, outputs] = line.split(":")
    nodes[node] = outputs.strip().split(" ")

def findAllPaths(node, visited):
    if node == "out":
        return 1
    total = 0
    for n in nodes[node]:
        if n not in visited:
            total += findAllPaths(n, visited)
        else:
            total += visited[n]
    visited[node] = total
    return total

result = findAllPaths("you", {})

print(result)

# Solution 539

