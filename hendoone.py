n = int(input())
string = [int(i) for i in input().split()]
print(string.index(max(string)) + 1)