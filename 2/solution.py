# Solved by checking if a number has even digit and then check if digit in first half is the same as second half.
def isInvalidNbr(string):
    if len(string) % 2 == 0:
        s, m = 0, len(string) // 2
        return string[0: m] == string[m:]
    return False

def getResult():
    # f = open("2/simple.txt", "r")
    f = open("2/input.txt", "r")
    sumOfInvalidNbr = 0
    for line in f:
        ranges = line.split(",")
        for r in ranges:
            [start, end] = r.split("-")
            for i in range(int(start), int(end) + 1):
                string = str(i)
                if string[0] == 0 or isInvalidNbr(string):
                    sumOfInvalidNbr += i

    return sumOfInvalidNbr
                       
print(getResult())
# Solution 30323879646