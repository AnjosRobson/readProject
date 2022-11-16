with open("file1.txt") as f1:
    content1 = f1.read()
    content1 = content1.split("\n")

with open("file2.txt") as f2:
    content2 = f2.read()
    content2 = content2.split("\n")

lines1 = []
lines2 = []
num = 1


for line1 in content1:
    lines1.append(line1)
    if num == 4:
        num = 1
        break

for line2 in content2:
    lines2.append(line2)
    if num == 4:
        break

loop = 0
erros = 0
for line in line1:
    if line == line2[loop]:
        erros = erros + 1
    loop = loop +1

print("erros", erros)

print(lines1)







