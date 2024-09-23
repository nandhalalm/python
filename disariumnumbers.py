num=int(input("enter the number"))
numstr1=str(num)
sum=0

for i in range (len(numstr1)):
    sum=sum+int(numstr1[i])**(i+1)

if sum==num:
    print("it is disarium",num)
else:
    print("not disarium",num)
    
