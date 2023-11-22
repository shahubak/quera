# a, b = map(int,input().split())

# d = 60 - b
# if 0 <= a <= 11:
#     s = 12 - a
# elif 0 <= b <= 59:
#     d = 60 - b

# if s == 12 and d == 60:
#     s = 0
#     d = 0

# if a <10 or b <10:
#     print(f"{s :02d}:{d :02d}")
# else:
#     print(f"{s}:{d}")


hour, min = [int(i) for i in input().split()]
min = "00" if min == 0 else str(60 - min)
hour = "00" if hour == 0 else str(12 - hour)

if len(min) < 2:
    min = "0" + min

if len(hour) < 2:
    hour = "0" + hour

print(f'{hour}:{min}')