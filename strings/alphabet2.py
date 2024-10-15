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

# Step 1: Get user input
s = input("Enter a string: ")


char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1


index = -1
for i in range(len(s)):
    if char_count[s[i]] == 1:
        index = i
        break


print(index)  

def MissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
    
l = [1, 2, 4, 5, 6, 7, 8, 9, 11, 13, 14, 16]
print(MissingNumbers(l))