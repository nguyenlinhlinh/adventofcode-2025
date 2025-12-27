
# f = open("6/input.txt", "r")
f = open("6/simple.txt", "r")
total = 0
worksheet = []
for line in f:
    if line[0] in ["+", "-", "*"]:
        a = []
        for i in line.split(" "):
            if i != "" and i != "\n":
                a.append(i)
        worksheet.append(a)
    else:
        a = []
        for i in line.split(" "):
            if i != "" and i != "\n":
                a.append(int(i))
        worksheet.append(a)
for i in worksheet:
    print(i)
result = [i for i in worksheet[0]]
print("result", result)

for r in range(1, len(worksheet) - 1):
    for c in range(len(worksheet[0])):
        print("row", r, "col", c, result)
        if worksheet[-1][c] == "+":
            print("+", r, c, result[c], worksheet[r][c])
            result[c] += worksheet[r][c]
        elif  worksheet[-1][c] == "*":
            print("*", r, c, result[c], worksheet[r][c])
            result[c] *= worksheet[r][c]
        print()
print(sum(result))

# Solution 4583860641327

