
n=int(input())
for i in range(1,n+1):
    for sp in range(n+1,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for sp in range(1,i+1):
        print(" ",end="")
    for j in range(n+1,i,-1):
        print("*",end=" ")
    print()