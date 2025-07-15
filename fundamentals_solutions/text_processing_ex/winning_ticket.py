def check_side_win(cur_ticket:str):
    winning_symbols = ("@", "$", "#", "^")
    left_side = ticket[:10]
    right_side = ticket[10:]

    for symbol in winning_symbols:
        for combo_count in range(10, 5, -1):
            combo = symbol * combo_count
            if combo in left_side and combo in right_side:
                if combo_count == 10:
                    return f'ticket "{cur_ticket}" - {combo_count}{symbol} Jackpot!'

                elif 6 <= combo_count <= 9:
                    return f'ticket "{cur_ticket}" - {combo_count}{symbol}'

    return f'ticket "{cur_ticket}" - no match'

tickets = [ticket.strip() for ticket in input().split(",")]
validated_tickets = list(map(lambda ticket: ticket if len(ticket) == 20 else "invalid ticket", tickets))

for ticket in validated_tickets:
    if ticket == "invalid ticket":
        print(ticket)
        continue

    result = check_side_win(ticket)
    print(result)
