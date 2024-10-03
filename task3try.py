
numbers_list = []
n = int(input("Enter size of list: "))

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers_list.append(num)


duplicate_numbers = []

# Find duplicates using nested loops
for i in range(len(numbers_list)):
    for j in range(i + 1, len(numbers_list)):
        if numbers_list[i] == numbers_list[j] and numbers_list[i] not in duplicate_numbers:
            duplicate_numbers.append(numbers_list[i])

# Print duplicate numbers
print("Duplicate numbers:", duplicate_numbers)


