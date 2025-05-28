import random

player_move = input("Please choose your move - rock, paper or scissors? ")
player_move = player_move.lower()
possible_moves = ["rock", "paper", "scissors"]

if player_move in "rock paper scissors":
    computer_move_idx = random.randint(0,2)
    computer_move = possible_moves[computer_move_idx]

    print(f"the computer chose {computer_move}")

    if player_move == computer_move:
        print("it's a draw!!1!")

    elif (player_move == "rock" and computer_move == "scissors") or \
        (player_move == "paper" and computer_move == "rock") or \
        (player_move == "scissors" and computer_move == "paper"):
        print("YOU WON!")

    else:
        print("you lost... against a computer...shame on you")

else:
    print("invalid input, run again to play")
