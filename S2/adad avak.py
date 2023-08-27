a = int(input())
b = int(input())

myl = []
for i in range(1,b+1):
    if (i % b != 0):
        myl.append(i)

print(myl)