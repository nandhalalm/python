numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd= odd + 1

print("Even numbers:", even)
print("Odd numbers:", odd)