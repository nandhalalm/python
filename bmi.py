weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

#print("Your BMI is", bmi)

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are healthy.")
elif 25 <= bmi < 29.9:
    print("You are over weight.")
elif 30 <= bmi < 34.9:
    print("You are severely over weight.")
elif 35 <= bmi < 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")

print("Your BMI is", bmi)