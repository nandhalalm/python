
my_tuple = ('a', 'b', 'c', 'd')

# Convert the tuple to a list
my_list = list(my_tuple)

# Change the second element to 'z'
my_list[1] = 'z'

# Convert the list back to a tuple
my_tuple_again = tuple(my_list)

print(my_tuple_again)  # Output: ('a', 'z', 'c', 'd')