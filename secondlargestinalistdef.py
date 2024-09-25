def secondlargest(numbers):
    return sorted(set(numbers))[-2]

numbers = [10, 20, 4, 45, 99]
print("The second largest number is:", secondlargest(numbers))
