# Solved by choosing the biggest number in in the range.
# To get the largest number with 12 digits iterate 12 times.
# For the first digit the search range should be from 0 to n - 11
# For the second digit the search range should be from postion of first digit to n - number of digit left to choose + 1

import heapq

f = open("3/input.txt", "r")
# f = open("3/simple.txt", "r")
total = 0
nbrOfDigits = 12
for line in f:
    line = line.strip()
    maxNbr = ""
    start, end = 0, len(line) - nbrOfDigits - 1
    while len(maxNbr) < nbrOfDigits:
        localMax = 0
        pos = start
        for i in range(start, end):
            nbr = int(line[i])
            if nbr > localMax:
                localMax = nbr
                pos = i
        maxNbr += line[pos]
        start = pos + 1
        end = len(line) - (nbrOfDigits - len(maxNbr)) + 1

    total +=int(maxNbr)

print(total)

# Solution 172981362045136
