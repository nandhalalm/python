def pyramid_alphabet_pattern(n):
    for i in range(1, n+1):
        print(" " * (n - i), end="")
        
        for j in range(i):
            print(chr(('a') + j), end=" ")
        
        print()  

pyramid_alphabet_pattern(5)