def iseven(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return iseven(n-2)

num = int(input("Enter a number: "))

if iseven(num):
    print(num, "is even")
else:
    print(num, "is odd")