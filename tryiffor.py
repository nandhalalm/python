# string="python"
# for i in string:
#     if i=="o":
#         print("if block")
#     else:
#         print(i)

# Diamond Star Pattern
n = 5

# Upper half of the diamond
for i in range(n):
    for j in range(0, n - i - 1):
        print(" ", end=" ")
    for k in range(0, 2 * i + 1):
        print("* ", end="")
    print()

# Lower half of the diamond
for i in range(n - 2, -1, -1):
    for j in range(0, n - i - 1):
        print(" ", end=" ")
    for k in range(0, 2 * i + 1):
        print("* ", end="")
    print()