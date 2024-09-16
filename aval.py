x = int(input())

myl = []
for j in range (x, 100000):  
    if x > 1:  
        for i in range (2, j):  
            if (j % i) != 0:  
                myl.append(j)  
                
        else:  
            break



print(myl)
