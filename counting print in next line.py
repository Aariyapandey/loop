n=int(input("enter the number of rows"))
num=1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num=num+1
    print() 
  
# while loop   
n=int(input("enter the number"))
num=1
row=1
while row<=n:
    col=1
    while col<=row:
        print(num,end=" ")
        col=col+1
        num=num+1
    print()
    row=row+1






# while loop 
n=int(input("enter the number"))
row=0
while row<=n-1:
    val=row+1
    dec=n-1
    col=0
    while col<=row:
        print(val,end=" ")
        val=val+dec
        col=col+1
    print()
    row=row+1    

# for loop         
n=int(input("enter the number of rows"))
for row in range(n):
    val=row+1
    dec=n-1
    for col in range(row+1):
        print(val,end=" ")
        val=val+dec
    print()








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








# for loop 
n=int(input("enter the number of rows"))
k=int(input("enter the number"))
for i in range(n):
    p=k
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ") 
        p=p-1
    k=k-1    
    print()   
    
# while loop 
n=int(input("enter the number of rows"))
k=int(input("enter the number"))
i=0
while i<=n:
    p=k
    j=0
    while j<=i:
        print(" ",end=" ")
        j=j+1
    while j<=n:
        print(p,end=" ")
        j=j+1
        p=p-1
    k=k-1
    print()
    i=i+1
    



# while loop 
n=int(input("enter a number"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    print()
    i=i+1      
    
# for loop 
n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()