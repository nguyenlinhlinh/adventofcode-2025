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

    newWorksheet = []
    a = []
    operators = []
    for row in rotated:
        nbr = ""
        if len(a) == 0:
            operators.append(row[-1])
        nbr = "".join([row[c] for c in range(len(row) - 1)]).strip()
        if nbr == "":
            newWorksheet.append(a)
            a = []
        else:
            a.append(int(nbr))
    newWorksheet.append(a)
    return newWorksheet, operators

def getResult():
    result = 0    
    f = open("6/input.txt", "r")
    # f = open("6/simple.txt", "r")
    worksheet = getInput(f)
    rotatedWorksheet, operators = rotateWorksheet(worksheet)
    for r in  range(len(rotatedWorksheet)):
        row = rotatedWorksheet[r]
        total = row[1]
        if operators[r] == '+':
            result += sum(row)
        else:
            total = 1
            for nbr in row:
                total *= nbr
            result += total
    return result

print(getResult())

# Solution 11602774058280