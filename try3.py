# numbers=[1,5,8,9,10,20,6,4,10,6]
# square=0
# squares=[]
# for i in numbers :
#     square=i**2
#     squares.append(square)
# print("the squares",squares)
n=5
for i in range (n):
    for j in range(0,i+1):
        print(" ",end=" ")
    for k in range(0,n-i):
        print(" *  ",end="")
    print()