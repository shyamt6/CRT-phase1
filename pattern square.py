r=4
for i in range(0,5):
    for s in range(1,r-i+1):
        print(" ",end=" ")
        for j in range(1,2*i):
            print("*",end=" ")
    print( )