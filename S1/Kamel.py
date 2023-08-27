
 
n=int(input())

mylist = []
for i in range(1,n):
    if(n%i==0):
        mylist.append(i)


if sum(mylist) == n:
    print("Yes")
else:
    print("No")
