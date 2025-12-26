# Solved by simple for loops since it only requires two digits.
import heapq

f = open("3/input.txt", "r")
# f = open("3/simple.txt", "r")
total = 0
for line in f:
    input = line.strip()
    maxNbr = 0
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            maxNbr = max(int(str(input[i]) + str(input[j])), maxNbr)
    total += maxNbr

print(total)

# Solution 17346