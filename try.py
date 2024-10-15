# year=int(input("enter the year"))
# if year%4==0:
#   print("is a leap year")
# else:
#   print("not a leap year")
class example:
   def add(self, a, b):
      x = a+b
      return x
   def add(self, a, b, c):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20,20))
print (obj.add(10,20,30))

# define parent class
class Parent: 
   def myMethod(self):
      print ('Calling parent method')

# define child class
class Child(Parent): 
   def myMethod(self):
      print ('Calling child method')

# instance of child
c = Child() 
# child calls overridden method
c.myMethod()


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)

def simple_generator(n):
    for i in range(n):
        yield i

# Example usage:
gen = simple_generator(5)
for num in gen:
    print(num)

def generate_numbers():
    """Generator function to yield numbers from 1 to 10."""
    for num in range(1, 11):  # Numbers from 1 to 10
        yield num  # Yield the current number

# Using the generator function
print("Numbers from 1 to 10:")
for number in generate_numbers():
    print(number)

