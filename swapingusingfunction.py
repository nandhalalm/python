def swap(a, b):
    a, b = b, a
    return a, b
a = 5
b = 10
a,b = swap(a, b)
print(f"After swapping: a = {a}, b = {b}")
