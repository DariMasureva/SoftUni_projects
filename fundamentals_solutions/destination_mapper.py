def separate_destinations(string_given):
    equal_expected = False
    slash_expected = False
    expected_symbol_idx = 0
    destination_list = []

    for idx, symbol in enumerate(string_given):

        if symbol == "=" and not slash_expected and not equal_expected:
            expected_symbol_idx = idx + 1
            equal_expected = True

        elif symbol == "=" and slash_expected:
            slash_expected = False
            equal_expected = True
            expected_symbol_idx = idx + 1
            
        elif symbol == "=" and equal_expected:
            cur_destination = string_given[expected_symbol_idx:idx]
            destination_list.append(cur_destination)
            expected_symbol_idx = idx + 1

        if symbol == "/" and not slash_expected and not equal_expected:
            expected_symbol_idx = idx + 1
            slash_expected = True

        elif symbol == "/" and equal_expected:
            equal_expected = False
            slash_expected = True
            expected_symbol_idx = idx + 1

        elif symbol == "/" and slash_expected:
            cur_destination = string_given[expected_symbol_idx:idx]
            destination_list.append(cur_destination)
            expected_symbol_idx = idx + 1

    return destination_list


def validate_destinations(destination_list):
    valid_dests = []

    for destination in destination_list:
        if destination:
            is_valid = False
            is_all_letters = destination.isalpha()
            is_first_upper = destination[0].isupper()
            length = len(destination)

            if is_all_letters and is_first_upper and length >= 3:
                is_valid = True

            if is_valid:
                valid_dests.append(destination)

    return valid_dests


def calculate_travel_points(destinations_list):
    total_points = 0

    for dest in destinations_list:
        total_points += len(dest)

    return total_points


initial_input = input()
destinations = separate_destinations(initial_input)
valid_destinations = validate_destinations(destinations)
total_travel_points = calculate_travel_points(valid_destinations)

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {total_travel_points}")
