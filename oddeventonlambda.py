# Define a lambda function
is_even = lambda n: n % 2 == 0

n = int(input("Enter a number: "))

# Call the lambda function with the user input
result = is_even(n)

print(f"The number {n} is {'even' if result else 'odd'}")