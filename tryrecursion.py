# def iseven(n):
#     if n == 0:
#       return True
#     elif n==1:
#       return False
#     else:
#        return iseven(n-2) 
       
# num =int(input("enter the elements"))
# if iseven(num):
#       print(num,"is even")
# else:
#     print(num,"is odd")  


#swap
def swap (a,b):
    a,b=b,a
    return a,b
a=5
b=10
a,b=swap(a,b)
print(f"After swapping: a = {a}, b = {b}")
    