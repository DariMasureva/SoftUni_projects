players = {}

while (command:=input()) != "Season end":

    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)

        if player not in players:
            players[player] = {}

        if position in players[player] and skill < players[player][position]:
            pass
        else:
            players[player][position] = skill

    else:
        player1, player2 = command.split(" vs ")

        if player1 in players and player2 in players:

            for cur_position, skill1 in players[player1].items():

                #check if they have any matching positions
                if cur_position in players[player2].keys():
                    skill2 = players[player2][cur_position]

                    if skill1 > skill2:
                        del players[player2]
                        break
                    elif skill1 < skill2:
                        del players[player1]
                        break

players = dict(sorted(players.items(), key=lambda item: item[0]))
players = dict(sorted(players.items(), key=lambda item: sum(item[1].values()), reverse=True))

for player, positions in players.items():
    positions = dict(sorted(positions.items(), key=lambda item: item[0]))
    positions = dict(sorted(positions.items(), key=lambda item: item[1], reverse=True))

    print(f"{player}: {sum(positions.values())} skill")
    for position, skill in positions.items():
        print(f"- {position} <::> {skill}")
