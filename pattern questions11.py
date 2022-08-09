n=int(input("enter the number of rows"))
for i in range(n):
    for j in range(i+1):
        if (i%2==0):
            print("*",end=" ")
        else:
            print("2",end=" ")
    print()            