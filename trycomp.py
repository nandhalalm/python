evenodd={num:num%2==0 for num in range(1,11)}
print(evenodd)

#dict fruits
fruits=['mango','apple','cherry','banana','date']
fruitlen={fruit:len(fruit)for fruit in fruits}
print(fruitlen)

#list comp
list1=[i for i in range(11) if i%2==0]
print(list1)

#matrix
matrix=[[j for j in range(3)] for i in range(4)]
print(matrix)

#set
list1=[1,2,3,4,5,6,7,8,9,10]
set1={element*3 for element in list1}
print(set1)

#set if
mylist=[1,2,3,4,5,6,7,8,9,10]
set1={element*3 for element in list1 if element%2==0}
print(set1)