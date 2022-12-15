# This is a number guessing game
import random

print("I am thinking of a number from 1 to 20")

secret_number = random.randint(1, 20)

print("Take a guess. You have 5 tries")

for guessesTaken in range(1, 6):
    guess = int(input())

    if guess < secret_number:
        print("Your number is too low")
    elif guess > secret_number:
        print("Your number is too high")
    else:
        break

if guess == secret_number:
    print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secret_number))
