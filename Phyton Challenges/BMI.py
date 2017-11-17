
height = float(input("What is your height in meters"))
weight = float(input("what is your weight in kilograms"))

BMI = weight/height**2

print("Your BMI is",BMI)

underweight = BMI<18.5
normalweight = 18.5 <= BMI < 25.0
overweight = 25.0 <= BMI < 30.0
obese = 30 <= BMI

if underweight:
    print("You are too skinny,go and eat some chicken fried rice and KFC")

elif normalweight:
    print("You are perfectly normal,go treat yourself to some ice cream")

elif overweight:
    print("You are kinda sorta really fat. Go and do some exercise and put the chips back in the cupboard")

elif obese:
    print("How are you so fat? You are obese, so go and do some exercise")

