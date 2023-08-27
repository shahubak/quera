a, b, c = map(int, input().split())



summ = a + b + c

if summ == 180 and a > 0 and b > 0 and c > 0:
    print("Yes")
elif summ < 180:
    print("No")
else:
    print("No")




