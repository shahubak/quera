a = int(input())
b = input().split()
c = input().split()

x = 0

for i in range(a):
    j = int(b[i]) * int(c[i])

    x += j

print(x)