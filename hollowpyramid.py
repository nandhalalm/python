size = 5

for i in range(size):
    for j in range(size - i - 1):
        print("  ", end="")
    for k in range(2 * i + 1):
        if i == 0 or k == 0 or j==size - i - 1 or k == 2 * i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()