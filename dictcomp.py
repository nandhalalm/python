keys=['a','b','c','d','e']
values=[1,2,3,4,5]
dict1={k:v for (k,v)in zip(keys,values)}
print(dict1)

#ex dict
a = {x: x**2 for x in [1,2,3,4,5]}
print (a)

#Ex 2

a = {x.upper(): x*3 for x in 'coding '}
print (a)

a="ABA"
dic = {x: {y: x + y for y in a} for x in a} 
print(dic)

