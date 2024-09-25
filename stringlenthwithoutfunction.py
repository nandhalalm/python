def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

user_input = input(" enter a string: ")
result = string_length(user_input)
print(f"The length of the string is: {result}")
