def getInput(f):
    worksheet = []
    for line in f:
        if line[0] in ["+", "-", "*"]:
            a = []
            for i in line.split(" "):
                if i != "" and i != "\n":
                    a.append(i)
            worksheet.append(line)
        else:
            line = line.strip("\n")
            worksheet.append(line)
    return worksheet

def rotateWorksheet(worksheet):
    rotated = [["" for i in range(len(worksheet))] for j in range(len(worksheet[0])) ]
    for r in range(0, len(worksheet)):
        for c in range(0, len(worksheet[0])):
            rotated[c][r] = worksheet[r][c]

    result = []
    a = []
    operator = []
    for r in rotated:
        print(r)
    for row in rotated:
        nbr = ""
        if len(a) == 0:
            a.append(row[-1])
        for c in range(len(row) - 1):
            if row[c] != "" and row[c] != "\n":
                nbr += row[c]
        if nbr.strip() == "":
            result.append(a)
            a = []
        else:
            a.append(int(nbr.strip(" ")))
    result.append(a)
    print("new")
    for r in result:
        print(r)
    return result

def getResult():
    result = 0    
    # f = open("6/input.txt", "r")
    f = open("6/simple.txt", "r")
    worksheet = getInput(f)
    rotatedWorksheet = rotateWorksheet(worksheet)
    for row in rotatedWorksheet:
        total = row[1]
        print(row)
        for n in range(2, len(row)):
            if row[0] == "*":
                total *= row[n]
            else:
                total += row[n]
        result += total
    return result

print(getResult())

# Solution 11602774058280