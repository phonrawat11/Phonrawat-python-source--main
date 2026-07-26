"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""
weight = float(input('Enter your weight (kg)'))
height = float(input('Enter your height (m)'))
BMI = weight / height ** 2
print("Your BMI =" , BMI)
if BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI <= 24.9:
    print("Normal weight")
elif BMI > 25 and BMI <= 29.9:
    print("Overweight")
else :
    print("Obese")

"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""

print("1. Convert THB to USD")
print("2. Convert USD to THB")
choice = input("Choose option: ")
if choice == "1":
    THB = float(input("Amount: "))
    THB_USD = THB / 35.5
    print("Convert to", THB_USD, "USD")
elif choice == "2":
    USD = float(input("Amount: "))
    USD_THB = USD * 35.5
    print("Convert to", USD_THB, "THB") 
