p1_name = input()
p2_name = input()

p1_points = 0
p2_points = 0
winner_name = ""
winner_points = 0

for _ in range(13):
    p1_input = input()
    if p1_input == "End of game":
        print(f"{p1_name} has {p1_points} points\n{p2_name} has {p2_points} points")
        break
    else:
        p2_input = input()
        if p2_input == "End of game":
            print(f"{p1_name} has {p1_points} points\n{p2_name} has {p2_points} points")
            break
        else:
            p1_turn = int(p1_input)
            p2_turn = int(p2_input)

        diff_turns = p1_turn - p2_turn

        if diff_turns > 0:
            p1_points += diff_turns
        elif diff_turns < 0:
            p2_points += abs(diff_turns)
        else:
            print("Number wars!")

            p1_last = int(input())
            p2_last = int(input())
            diff_turns = p1_last - p2_last

            if diff_turns > 0:
                winner_name = p1_name
                winner_points = p1_points
            else:
                winner_name = p2_name
                winner_points = p2_points

            print(f"{winner_name} is winner with {winner_points} points")
            break
