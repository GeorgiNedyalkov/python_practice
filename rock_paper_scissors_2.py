# this is a rock, paper, scissors game implementation 2.0
import random, sys

print("ROCK 🤘, PAPER 🧻, SCISSORS 👧👧")

wins = 0
losses = 0
ties = 0

# player game loop
while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))

    while True:
        print("Enter your move: r, p, s, or q to quit")
        player_move = input()
        if player_move == "q":
            print("Thank you for playing! 🙋‍♂️")
            sys.exit()
        if player_move == "r" or player_move == "p" or player_move == "s":
            break

    # display player choice:
    if player_move == "r":
        print("ROCK versus...")
    elif player_move == "p":
        print("PAPER versus...")
    elif player_move == "s":
        print("SCISSORS versus...")

    # display computer choice:
    computer_choice = random.randint(1, 3)
    computer_move = ""

    if computer_choice == 1:
        computer_move = "r"
        print("ROCK")
    elif computer_choice == 2:
        computer_move = "p"
        print("PAPER")
    elif computer_choice == 3:
        computer_move = "s"
        print("SCISSORS")

    # display and record the win/lose/tie:
    if player_move == computer_move:
        print("It's a tie")
        ties = ties + 1
    elif player_move == "r" and computer_move == "p":
        print("You lose!")
        losses = losses + 1
    elif player_move == "r" and computer_move == "s":
        print("You win!")
        wins = wins + 1
    elif player_move == "p" and computer_move == "s":
        print("You lose!")
        losses = losses + 1
    elif player_move == "p" and computer_move == "r":
        print("You win!")
        wins = wins + 1
    elif player_move == "s" and computer_move == "r":
        print("You lose!")
        losses = losses + 1
    elif player_move == "s" and computer_move == "p":
        print("You win!")
        wins = wins + 1
