def armstrong_recursive(num, power):
    if num == 0:
        return 0
    lastdigit = num % 10
    return (lastdigit ** power) + armstrong_recursive(num // 10, power)

def is_armstrong(num):
    power = len(str(num))  
    return num == armstrong_recursive(num, power)

num = int(input("Enter a number: "))


if is_armstrong(num):
    print(num, "is an Armstrong Number.")
else:
    print(num, "is not an Armstrong Number.")