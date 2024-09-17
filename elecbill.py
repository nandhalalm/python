units = int(input("Enter the number of units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
     bill = 100 * 5 +( units-100 )*10
else:
     bill = 100 * 5 + 100 * 10 +(units-200)*15

print("Your electricity bill is:", bill)