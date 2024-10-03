#def sum_list(lst):
 #   return sum(lst)
#numbers = [1, 2, 3, 4, 5]
#result = sum_list(numbers)
#print(result) 

def list1(lst):
    if len(lst)==0:
        return 0
    else:
        return lst[0]+list1(lst[l:])
    
numbers = [1, 2, 3, 4, 5]
result = list1(numbers)
print(result)