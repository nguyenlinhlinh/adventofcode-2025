f = open("11/input.txt", "r")
# f = open("11/simple.txt", "r")
# f = open("11/simple2.txt", "r")
nodes = {}
for line in f:
    line = line.strip()
    [node, outputs] = line.split(":")
    nodes[node] = outputs.strip().split(" ")

def findAllPaths(start, end, excluded, visited):
    if start == end:
        return 1
    if start in excluded:
        return 0
    count = 0
    for n in nodes[start]:
        if n not in visited:
            count += findAllPaths(n, end, excluded, visited)
        else:
            count += visited[n]
    visited[start] = count
    return count

nbrOfPaths = {}
nbrOfPaths["svr-dac"] = findAllPaths("svr", "dac",set(["fft", "out"]), {})
nbrOfPaths["dac-fft"] = findAllPaths("dac", "fft",set(["svr", "out"]), {})
nbrOfPaths["fft-out"] = findAllPaths("fft", "out",set(["dac", "svr"]), {})
nbrOfPaths["svr-fft"] = findAllPaths("svr", "fft",set(["out", "dac"]), {})
nbrOfPaths["fft-dac"] = findAllPaths("fft", "dac", set(["svr", "out"]), {})
nbrOfPaths["dac-out"] = findAllPaths("dac", "out", set(["fft", "svr"]), {})  

total = (nbrOfPaths["svr-dac"] * nbrOfPaths["dac-fft"] * nbrOfPaths["fft-out"] + nbrOfPaths["svr-fft"] * nbrOfPaths["fft-dac"] * nbrOfPaths["dac-out"])
print(total)

# Solution 413167078187872

