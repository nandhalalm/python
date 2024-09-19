# pyramid
n=5
for i in range (n):
    for j in range(0,i+1):
        print(" ",end=" ")
    for k in range(0,n-i):
        print(" *  ",end="")
    print()
#half pyramid
n=5
for i in range (n):
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(0,i+1):
        print(" *  ",end="")
    print()