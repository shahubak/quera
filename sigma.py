a = int(input())
b = int(input())
i = -10
j = 1
hasel = 0

for item in range(i, b + 1):
    for item1 in range(j, a + 1):
        s = (item + item1) ** 3 / item1 ** 2
        hasel += int(s)

print(hasel)