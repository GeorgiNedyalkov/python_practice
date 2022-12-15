print("What is your age?")

age = int(input())

if age <= 12:
    print("Oh you are a baby")
elif age >= 13 and age <= 19:
    print("Hello teens")
elif age >= 20 and age < 30:
    print("Growing up is a trap")
else:
    print("Hi grandpa")
