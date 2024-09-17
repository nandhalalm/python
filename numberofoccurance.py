inputstring = input("Enter a string: ")
character = input("Enter the character to count: ")
count = 0

for i in inputstring:
    if i == character:
        count += 1

print(f"The character '{character}' appears {count} times in the string.")