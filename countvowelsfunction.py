def vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

input1 = input("Please enter a string: ")
result = vowels(input1)
print(f"The number of vowels in the string is: {result}")
