# n = int(input())

# myl = []
# y = 0
# for i in range(n):
#     x = input()
#     myl.append(x)
# for j in range(0, n-1):
#     if x[j] != x[j+1]:
#         y += 1

# print(y)

status = 0
n = int(input())
names = [input() for i in range(n)]

for i in range(0, n - 1):
    if names[i] != names[i + 1]:
        status += 1

print(status)