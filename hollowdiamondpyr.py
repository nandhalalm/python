rows = 5 

# Upper part of the diamond
for i in range(rows):
    print(' ' * (rows - i - 1), end='')  
    if i == 0:
        print('*')
    else:
        print('*' + ' ' * (2 * i - 1) + '*')

# Lower part of the diamond
for i in range(rows - 2, -1, -1):
    print(' ' * (rows - i - 1), end='')  
    if i == 0:
        print('*')
    else:
        print('*' + ' ' * (2 * i - 1) + '*')
