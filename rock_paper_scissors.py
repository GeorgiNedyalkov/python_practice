import random

print("Hello, let's play rock paper scissors. Make your choice")

player_choice = input().lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

if player_choice == "rock":
    if computer_choice == "paper":
        print("Computer wins this one")
    elif computer_choice == "scissors":
        print("Player wins. Fudge technology!")
    elif computer_choice == "rock":
        print("This round is equal. Well played try again!")
elif player_choice == "paper":
    if computer_choice == "scissors":
        print("Computer wins this one")
    elif computer_choice == "rock":
        print("Player wins. Fudge technology!")
    elif computer_choice == "paper":
        print("This round is equal. Well played try again!")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("Computer wins this one")
    elif computer_choice == "paper":
        print("Player wins. Fudge technology!")
    elif computer_choice == "scissors":
        print("This round is equal. Well played try again!")
else:
    print("Wrong choice! Please try again. You can choose rock, paper or scissors")


print("Computer chose: " + computer_choice)
print("Player chose: " + player_choice)
