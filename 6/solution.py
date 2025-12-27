def getInput(f):
    total = 0
    worksheet = []
    operators = []
    for line in f:
        if line[0] in ["+", "*"]:
            for i in line.strip().split(" "):
                if i:
                    operators.append(i)
        else:
            a = []
            for i in line.strip().split(" "):
                if i:
                    a.append(int(i))
            worksheet.append(a)
    return worksheet, operators


def getResult():
    f = open("6/input.txt", "r")
    # f = open("6/simple.txt", "r")
    worksheet, operators = getInput(f)
    result = [i for i in worksheet[0]]
    for r in range(1, len(worksheet)):
        for c in range(len(worksheet[0])):
            if operators[c] == "+":
                result[c] += worksheet[r][c]
            elif operators[c] == "*":
                result[c] *= worksheet[r][c]
    return sum(result)
print(getResult())

# Solution 4583860641327

