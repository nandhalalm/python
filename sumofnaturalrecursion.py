def recursum(n):
    if n % 2==0:
        return "even"
    else:
        return n + recureven(n-1)
    
num = int(input("natural numbers"))
result=recursum(num)
print("sum is",num,"is",result)

