h = float(input("Enter your height in meters:"))
w = float(input("Enter your weight:"))
BMI = w/h**2
print("Your BMI is: ",BMI)
if BMI <= 18.4:
     print("Your underweight")
elif BMI <=24.9:
     print("Your healthy")
elif BMI <=29.9:
     print("you are overweight")
elif BMI <=39.9:
     print("Your obese")
else:
     print("invalid input")