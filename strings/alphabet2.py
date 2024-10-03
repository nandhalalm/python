n=5
for i in range(1,n+1):
    print(' ' * (n-i),end=' ')
    for j in range(i):
        print(chr(64 +i),end=' ')

    print()

# n=4

# for i in range(1,n+1):
#     print(' '*(n-i)+' *' * i)

set1=""
print(type(set1))


#zpattern

n = 5

if n < 3:
    print("Size must be at least 3")
else:
   
    print('*' * n)
    
    for i in range(1, n - 1):
        print(' ' * (n - i - 1) + '*')
    
    print('*' * n)
