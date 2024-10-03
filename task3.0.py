
numbers_list = []

n = int(input("Enter the size of the list: "))

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers_list.append(num)

unique_numbers = []

for num in numbers_list:
    if numbers_list.count(num) == 1:
        unique_numbers.append(num)

print("Numbers that appear exactly once:", unique_numbers)
