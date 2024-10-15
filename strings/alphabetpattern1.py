# n = 5
# alphabet = "abcde"

# for i in range(1, n+1):
#     print(" " * (n - i), end="    ")
#     print(alphabet[:i])


# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i), end=" ")
    
#     # Print letters from A to the ith letter
#     for j in range(i):
#         print(chr(97 + j), end=" ")  
    
#     print()  
n = 5
alphabet = "abcde"

for i in range(1, n + 1):
    print(" " * (n - i), end=" ")

    for j in range(i):
        print(alphabet[j], end=" ")  
    
    print()  
