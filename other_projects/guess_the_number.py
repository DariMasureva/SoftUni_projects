import random

computer_number = random.randint(0, 100)
total_guesses = int(input("in how many tries can you guess the computers number? "))
bet = int(input("you could place a bet, if you'd like. for every additional try the bet doubles >:) "))
current_guess_count = 1

player_guess = -1

while player_guess != computer_number:

    player_guess = int(input("your guess: "))

    if total_guesses == 0:
        print("just stop cheating and play the game")
        break

    if player_guess - computer_number > 70:
        print("WAYY TOO HIGH")
    elif player_guess - computer_number > 50:
        print("too high, not even close")
    elif player_guess - computer_number > 30:
        print("too high")
    elif player_guess - computer_number > 10:
        print("high but not too far off")
    elif player_guess - computer_number > 5:
        print("too high but close")
    elif player_guess - computer_number > 1:
        print("too high but sooo close")
    elif player_guess - computer_number < -70:
        print("WAYY TOO LOW")
    elif player_guess - computer_number < -50:
        print("too low, not even close")
    elif player_guess - computer_number < -30:
        print("too low")
    elif player_guess - computer_number < -10:
        print("low but not too far off")
    elif player_guess - computer_number < -5:
        print("too low but close")
    elif player_guess - computer_number < -1:
        print("too low but sooo close")

    current_guess_count += 1

    if current_guess_count > total_guesses:
        bet *= 2

else:

    if current_guess_count > total_guesses and bet:
        print(f"YOU GUESSED THE NUMBER IN {current_guess_count} TRIES AND LOST {bet}. Weren't {total_guesses} guesses "
              f"enough for you??")
    elif current_guess_count > total_guesses and not bet:
        print(f"YOU GUESSED THE NUMBER IN {current_guess_count}. Weren't {total_guesses} guesses "
              f"enough for you??")
    elif current_guess_count == total_guesses and bet:
        print(f"you were so close to losing your money, but your prediction was accurate, so I'll let you go this time")
    elif current_guess_count == total_guesses:
        print("you should have placed a bet, because your precision is phenomenal")
    elif current_guess_count < total_guesses and bet:
        print(f"EVEN BETTER THAN EXPECTED!! You guessed  the number in {current_guess_count} tries and take {bet} of "
              f"my sweet precious coins")
    else:
        print(f"EVEN BETTER THAN EXPECTED!! You guessed  the number in {current_guess_count} tries but you get none "
              f"of my sweet coins")
