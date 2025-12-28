# f = open("2/simple.txt", "r")
f = open("2/input.txt", "r")
sumOfInvalidNbr = 0
count = 0
for line in f:
    ranges = line.split(",")
    for r in ranges:
        [start, end] = r.split("-")
        s, e = int(start), int(end)
        minDigits = len(start)
        maxDigits = len(end) + 1
        i = 1
        invalidNumbers = set()
        while len(str(i)) <= maxDigits // 2:
            for digits in range(minDigits, maxDigits):
                rep = digits // len(str(i))
                if rep <= 1:
                    continue
                nbr = int(str(i) * rep)
                if nbr >= s and nbr <= e:
                    invalidNumbers.add(nbr)
            i+= 1
        sumOfInvalidNbr += sum(invalidNumbers)
print("sumOfInvalidNbr", sumOfInvalidNbr)
# Solution 43872163557