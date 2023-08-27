
def squer (n):
    print(n * "*")
    for i in range(n-2):
        print("*" + (n-2) * " " + "*")
    print(n * "*")

sq = int(input())

if sq < 3:
    pass
else:
    squer(sq)

