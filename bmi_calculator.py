# create a program that calculates the person's BMI based on their height and weight
# you need to be able to tell the person whether their under, normal, overweight or obese

weight = int(input("What is your weight (in lbs)? "))
height = int(input("What is your height (in inches)? "))

bmi = round(float(weight / (height * height) * 703), 2)

print("Your weight is " + str(weight) + " and your height is " + str(height))  
print("Your BMI is " + str(bmi))

def calculate_bmi():
	if bmi <= 18.5: 
		print("You are underweight. Eat more!")
	elif bmi >= 18.5 and bmi <= 24.9: 
		print("You have a normal weight. Good job!")
	elif bmi >= 25 and bmi <= 29.9: 
		print("You are overweight. Go workout fatty!")
	elif bmi >= 30: 
		print("You are obese. Eat healthier!")

calculate_bmi()