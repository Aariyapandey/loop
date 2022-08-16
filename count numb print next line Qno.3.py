# for loop
n=int(input("enter the number of rows"))
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()
    
# while loop  
n=int(input("enter the number of rows"))
row=0
while row<=n:
    col=1
    while col<=n-row:
        print(col,end=" ")
        col=col+1
    print()
    row=row+1