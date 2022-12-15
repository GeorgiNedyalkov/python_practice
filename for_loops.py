# print jimmy five times five times
print("My name is")
for i in range(5):
    print("Jimmy Five times(" + str(i) + ")")

# sum all numbers from 1 to 100
print("What is the sum of all number from 1 to 100")
sum = 0
for i in range(101):
    sum += i

print("The answer is " + str(sum))

# print all even numbers from 0 to 100
def printEvenNums():
    for num in range(0, 100, 2):
        print(num)


# print numbers from 10 to 1
def countdown():
    print("Initiating countdown sequence...")

    for num in range(10, 0, -1):
        print(num)

    print("Houson we have a lift of 🚀")


countdown()
