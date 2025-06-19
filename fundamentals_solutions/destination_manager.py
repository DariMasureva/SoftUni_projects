def separate_destinations(string_given):
    first_equal_found = False
    first_slash_found = False
    destination_list = []
    cur_destination = ""

    for symbol in string_given:

        if (first_slash_found and symbol != "/") or (first_equal_found and symbol != "="):
            cur_destination += symbol

        if symbol == "=" and not first_equal_found and not first_slash_found:
            first_equal_found = True
        elif symbol == "=" and first_equal_found and cur_destination:
            first_equal_found = False
            destination_list.append(cur_destination)
            cur_destination = ""

        elif symbol == "/" and not first_slash_found and not first_equal_found:
            first_slash_found = True
        elif symbol == "/" and first_slash_found and cur_destination:
            first_slash_found = False
            destination_list.append(cur_destination)
            cur_destination = ""

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
