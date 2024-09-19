
n = 5

# First pyramid 
for i in range(n - 1): 
    for j in range(0, n - i):
        print(" ", end=" ")
    for k in range(0, i + 1):
        print(" *  ", end="")
    print()

# Second pyramid
for i in range(n):
    for j in range(0, i + 1):
        print(" ", end=" ")
    for k in range(0, n - i):
        print(" *  ", end="")
    print()
